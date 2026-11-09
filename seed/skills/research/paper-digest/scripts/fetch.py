import argparse
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


def fetch(query):
    params = urllib.parse.urlencode({
        'search_query': query,
        'max_results': 8,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    })
    request = urllib.request.Request(
        'https://export.arxiv.org/api/query?' + params,
        headers={'User-Agent': 'paper-digest/0.2 (academic coursework)'},
    )
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt:
                raise
            delay = error.headers.get('Retry-After', '10')
            time.sleep(min(int(delay), 30) if delay.isdigit() else 10)
        except (urllib.error.URLError, TimeoutError):
            if attempt:
                raise
            time.sleep(10)


def collect(queries):
    namespace = {'a': 'http://www.w3.org/2005/Atom'}
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    papers = {}
    errors = []
    for index, query in enumerate(queries):
        if index:
            time.sleep(3)
        try:
            root = ET.fromstring(fetch(query))
            for entry in root.findall('a:entry', namespace):
                def value(name):
                    return ' '.join((entry.findtext('a:' + name, '', namespace)).split())
                paper_id = value('id').rsplit('/abs/', 1)[-1]
                published = value('published')
                if not published or datetime.fromisoformat(published.replace('Z', '+00:00')) < cutoff:
                    continue
                if paper_id == value('id'):
                    continue
                papers[paper_id] = {
                    'id': paper_id,
                    'url': 'https://arxiv.org/abs/' + paper_id,
                    'title': value('title'),
                    'published': published,
                    'authors': [a.findtext('a:name', '', namespace) for a in entry.findall('a:author', namespace)],
                    'abstract': value('summary'),
                }
        except (urllib.error.URLError, TimeoutError, ET.ParseError, ValueError) as error:
            errors.append({'query': query, 'error': str(error)})
    return {
        'status': 'source_error' if errors else ('ok' if papers else 'empty'),
        'window_days': 7,
        'queries': queries,
        'papers': list(papers.values()),
        'errors': errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('queries', nargs='+')
    args = parser.parse_args()
    if len(args.queries) > 3:
        parser.error('Не больше трёх запросов за запуск')
    started = time.monotonic()
    result = collect(args.queries)
    result['elapsed_seconds'] = round(time.monotonic() - started, 3)
    result['recorded_at'] = datetime.now(timezone.utc).isoformat()
    home = Path(os.environ.get('HERMES_HOME', Path.home() / '.hermes'))
    path = home / 'workspace' / 'paper-digest-runs' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
    path.mkdir(parents=True, exist_ok=True)
    output = path / 'source.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'source_file': str(output), **result}, ensure_ascii=False))


if __name__ == '__main__':
    main()
