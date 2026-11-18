import argparse
import contextlib
import io
import json
import os
import re
import time
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from search import collect, validate_query


MODEL = 'nvidia/nemotron-3-ultra-550b-a55b:free'
SKILL_DIR = Path(__file__).resolve().parents[1]


def read_json(text):
    value = text.strip()
    if value.startswith('```') and value.endswith('```'):
        value = '\n'.join(value.splitlines()[1:-1])
    result = json.loads(value)
    if not isinstance(result, dict):
        raise ValueError('Модель вернула JSON другого типа')
    return result


def ask_agent(stage, data, calls):
    from dotenv import load_dotenv
    from hermes_state import SessionDB
    from run_agent import AIAgent

    prompt = (SKILL_DIR / 'prompts' / (stage + '.txt')).read_text()
    prompt += '\nДАННЫЕ\n' + json.dumps(data, ensure_ascii=False)
    home = Path(os.environ.get('HERMES_HOME', '/opt/data'))
    load_dotenv(home / '.env', override=False)
    key = os.environ.get('OPENROUTER_API_KEY')
    if not key:
        raise RuntimeError('Не настроен OPENROUTER_API_KEY')
    database = SessionDB()
    agent = None
    call = {'stage': stage, 'tokens': {}, 'usage_available': False}
    calls.append(call)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            agent = AIAgent(
                model=MODEL, provider='openrouter', api_key=key,
                base_url='https://openrouter.ai/api/v1',
                enabled_toolsets=[], max_iterations=1, max_tokens=2048,
                reasoning_config={'effort': 'none'}, quiet_mode=True,
                skip_context_files=True, skip_memory=True, skip_background_review=True,
                run_budget_seconds=60, session_db=database, platform='cli',
            )
            result = agent.run_conversation(prompt)
    except Exception as error:
        detail = str(error).replace(key, '[REDACTED]')
        raise RuntimeError('Ошибка Hermes на этапе ' + stage + ': ' + detail[:500]) from error
    finally:
        if agent is not None:
            agent.close()
        database.close()
    call.update({
        'session_id': result.get('session_id'),
        'tokens': {'input': result.get('input_tokens', 0), 'output': result.get('output_tokens', 0)},
        'api_calls': result.get('api_calls', 0),
        'completed': result.get('completed'),
        'usage_available': 'input_tokens' in result and 'output_tokens' in result,
    })
    if result.get('failed') or result.get('completed') is False:
        detail = result.get('error') or result.get('final_response') or 'Hermes завершился без ответа'
        raise RuntimeError('Ошибка модели на этапе ' + stage + ': ' + detail[:500])
    return read_json(result['final_response'])


def normalized(text):
    return ' '.join(text.casefold().split())


def verified_selection(answer, papers):
    selected = answer.get('selected')
    if not isinstance(selected, list):
        raise ValueError('Модель не вернула список selected')
    by_url = {paper['url']: paper for paper in papers}
    accepted = []
    rejected = []
    seen = set()
    for item in selected:
        if not isinstance(item, dict):
            rejected.append('Запись не является объектом')
            continue
        url = item.get('url')
        paper = by_url.get(url) if isinstance(url, str) else None
        reason = item.get('reason')
        evidence = item.get('evidence')
        if paper is None:
            rejected.append('Ссылка отсутствует в ответе arXiv')
            continue
        if not isinstance(reason, str) or not 1 <= len(reason.strip()) <= 500:
            rejected.append('Не указано краткое обоснование отбора')
            continue
        if not isinstance(evidence, str) or not 1 <= len(evidence.split()) <= 15:
            rejected.append('Не указан короткий фрагмент аннотации')
            continue
        abstract = normalized(paper['abstract'])
        if normalized(evidence) not in abstract:
            rejected.append('Приведённого фрагмента нет в аннотации')
            continue
        if not re.search(r'\b(?:web|browser)\w*', abstract):
            rejected.append('Аннотация не подтверждает связь с вебом')
            continue
        if not re.search(r'\b(?:adapt|personali[sz]|reconfigur)\w*', abstract):
            rejected.append('Аннотация не подтверждает адаптацию или персонализацию')
            continue
        if url not in seen:
            seen.add(url)
            article = paper.copy()
            article['reason'] = reason.strip()
            article['evidence'] = evidence.strip()
            accepted.append(article)
    return accepted[:3], rejected


def render(record):
    found = record.get('returned_count', 0)
    selected = record.get('selected', [])
    lines = [f'Проверка arXiv: получено {found}, отобрано {len(selected)}.', '']
    if record['status'] == 'error':
        lines.append('Проверка не завершена: ' + record['error'])
    elif not record['selected']:
        lines.append('За выбранный период подходящих работ в полученной выдаче не найдено.')
    for paper in selected:
        lines.extend([
            paper['title'],
            'Авторы: ' + ', '.join(paper['authors']),
            'Дата: ' + paper['published'][:10],
            'Ссылка: ' + paper['url'],
            'Связь с темой: ' + paper['reason'],
            '',
        ])
    if record.get('rejected'):
        lines.append('Часть предложений модели исключена при проверке данных.')
    if record.get('query'):
        lines.extend(['', 'Запрос: ' + record['query']])
    lines.append(f"Период: {record['days']} суток.")
    return '\n'.join(lines).strip() + '\n'


def run(home, days):
    started = time.monotonic()
    record = {
        'started_at': datetime.now(timezone.utc).isoformat(),
        'model': MODEL, 'days': days, 'status': 'error',
        'calls': [], 'selected': [], 'rejected': [],
    }
    try:
        topic = (home / 'memories' / 'MEMORY.md').read_text()
        query = ask_agent('query', {'topic': topic}, record['calls']).get('query')
        if not isinstance(query, str):
            raise ValueError('Модель не вернула поисковый запрос')
        record['query'] = validate_query(query)
        result = collect(record['query'], days)
        record['returned_count'] = len(result['papers'])
        if result['papers']:
            answer = ask_agent('select', {'topic': topic, 'papers': result['papers']}, record['calls'])
            record['selected'], record['rejected'] = verified_selection(answer, result['papers'])
        record['status'] = 'ok' if record['selected'] else 'empty'
    except (OSError, ValueError, RuntimeError, argparse.ArgumentTypeError, ET.ParseError) as error:
        record['error'] = str(error)
    record['duration_seconds'] = round(time.monotonic() - started, 3)
    usage_available = all(call.get('usage_available', False) for call in record['calls'])
    if usage_available:
        record['input_tokens'] = sum(call['tokens'].get('input', 0) for call in record['calls'])
        record['output_tokens'] = sum(call['tokens'].get('output', 0) for call in record['calls'])
    else:
        record['input_tokens'] = None
        record['output_tokens'] = None
    return record, render(record)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=7)
    args = parser.parse_args()
    if args.days < 1:
        parser.error('--days должен быть положительным')
    home = Path(os.environ.get('HERMES_HOME', '/opt/data'))
    record, text = run(home, args.days)
    output = home / 'paper-digest'
    output.mkdir(exist_ok=True)
    name = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    (output / (name + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2))
    (output / (name + '.md')).write_text(text)
    print(text, end='')
    return 1 if record['status'] == 'error' else 0


if __name__ == '__main__':
    raise SystemExit(main())
