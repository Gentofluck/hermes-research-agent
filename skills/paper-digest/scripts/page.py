import argparse
import json
import urllib.parse
import urllib.request
from html.parser import HTMLParser


class PageText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.hidden = 0
        self.title = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        if tag in ('script', 'style'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if not self.hidden:
            self.text.append(data)


def arxiv_url(value):
    url = urllib.parse.urlsplit(value)
    if url.scheme != 'https' or url.hostname not in ('arxiv.org', 'info.arxiv.org'):
        raise argparse.ArgumentTypeError('Ожидается HTTPS-страница arXiv')
    if url.username or url.password or url.port not in (None, 443):
        raise argparse.ArgumentTypeError('Адрес не должен содержать учётные данные или другой порт')
    return value


def read_page(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'adaptive-ui-paper-digest/1.0'})
    with urllib.request.urlopen(request, timeout=20) as response:
        arxiv_url(response.url)
        payload = response.read(1_000_001)
        if len(payload) > 1_000_000:
            raise ValueError('Страница превышает ограничение в 1 МБ')
        parser = PageText()
        parser.feed(payload.decode('utf-8', errors='replace'))
        text = ' '.join(' '.join(parser.text).split())
        return {
            'url': response.url,
            'http_status': response.status,
            'title': ' '.join(parser.title).strip(),
            'text': text[:6000],
            'truncated': len(text) > 6000,
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=arxiv_url)
    args = parser.parse_args()
    try:
        result = read_page(args.url)
    except (OSError, ValueError, argparse.ArgumentTypeError) as error:
        print(json.dumps({'url': args.url, 'error': str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
