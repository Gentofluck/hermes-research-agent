import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone


API_URL = 'https://export.arxiv.org/api/query'
ATOM = {'a': 'http://www.w3.org/2005/Atom'}
RESULT_LIMIT = 20
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}


def download(query):
    parameters = {
        'search_query': query,
        'max_results': RESULT_LIMIT,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }
    url = API_URL + '?' + urllib.parse.urlencode(parameters)
    request = urllib.request.Request(
        url,
        headers={'User-Agent': 'adaptive-ui-paper-digest/1.0'},
    )

    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if attempt == 1 or error.code not in RETRYABLE_HTTP_CODES:
                raise

            retry_after = error.headers.get('Retry-After', '3')
            delay = 3
            if retry_after.isdigit():
                delay = max(3, min(int(retry_after), 30))
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError):
            if attempt == 1:
                raise
            time.sleep(3)


def read_text(element, field):
    value = element.findtext('a:' + field, '', ATOM)
    return ' '.join(value.split())


def parse_publication(entry):
    address = urllib.parse.urlsplit(read_text(entry, 'id'))
    if address.hostname not in ('arxiv.org', 'export.arxiv.org'):
        raise ValueError('В ответе arXiv указан неизвестный источник')
    if not address.path.startswith('/abs/'):
        raise ValueError('arXiv вернул запись без идентификатора статьи')

    authors = []
    for author in entry.findall('a:author', ATOM):
        authors.append(read_text(author, 'name'))

    return {
        'title': read_text(entry, 'title'),
        'authors': authors,
        'published': read_text(entry, 'published'),
        'url': 'https://arxiv.org' + address.path,
        'abstract': read_text(entry, 'summary'),
    }


def parse_feed(payload, since, until):
    feed = ET.fromstring(payload)
    if feed.tag != '{http://www.w3.org/2005/Atom}feed':
        raise ValueError('Ответ arXiv не является Atom-лентой')

    publications = []
    for entry in feed.findall('a:entry', ATOM):
        publication = parse_publication(entry)
        published_at = datetime.fromisoformat(publication['published'].replace('Z', '+00:00'))
        if published_at.tzinfo is None:
            raise ValueError('В дате публикации не указан часовой пояс')
        if since <= published_at <= until:
            publications.append(publication)
    return publications


def collect(query, days):
    now = datetime.now(timezone.utc)
    since = now - timedelta(days=days)
    publications = parse_feed(download(query), since, now)

    status = 'empty'
    if publications:
        status = 'ok'
    return {
        'status': status,
        'query': query,
        'days': days,
        'limit': RESULT_LIMIT,
        'papers': publications,
    }


def validate_query(value):
    query = value.strip()
    if not re.search(r'\b(?:all|ti|abs):\s*\S', query):
        raise argparse.ArgumentTypeError('Нужны тематические условия в полях ti:, abs: или all:; одной категории недостаточно')
    return query


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True, type=validate_query)
    parser.add_argument('--days', type=int, default=7)
    arguments = parser.parse_args()
    query = arguments.query
    if arguments.days < 1:
        parser.error('--days должен быть положительным числом')

    started_at = time.monotonic()
    try:
        result = collect(query, arguments.days)
    except (urllib.error.URLError, TimeoutError, ET.ParseError, ValueError) as error:
        result = {
            'status': 'error',
            'query': query,
            'days': arguments.days,
            'error': str(error),
            'papers': [],
        }

    result['elapsed_seconds'] = round(time.monotonic() - started_at, 3)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['status'] == 'error':
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
