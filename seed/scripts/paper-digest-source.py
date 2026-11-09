import json
import os
import subprocess
import sys
from pathlib import Path

from tools.cronjob_prompt_scan import _scan_cron_prompt

home = Path(os.environ['HERMES_HOME'])
memory = (home / 'memories' / 'MEMORY.md').read_text()
line = next(line for line in memory.splitlines() if line.startswith('Запросы arXiv:'))
queries = json.loads(line.split(':', 1)[1].strip())
if not isinstance(queries, list) or not 1 <= len(queries) <= 3 or not all(isinstance(q, str) for q in queries):
    raise ValueError('В памяти должны быть от одного до трёх запросов arXiv')
result = subprocess.run([
    sys.executable,
    str(home / 'skills' / 'research' / 'paper-digest' / 'scripts' / 'fetch.py'),
    *queries,
], check=True, capture_output=True, text=True)
data = json.loads(result.stdout)
papers = []
excluded = []
for paper in data['papers']:
    if _scan_cron_prompt(json.dumps(paper, ensure_ascii=False)):
        excluded.append(paper['id'])
    else:
        papers.append(paper)
data['papers'] = papers
data['excluded_ids'] = excluded
data['incomplete'] = bool(excluded or data['errors'])
if excluded and not papers and not data['errors']:
    data['status'] = 'filtered'
data['output_instructions'] = (
    'Выбери до трёх статей по темам из памяти. Ответ на русском. '
    'Для каждой записи строго четыре строки: Название: точный title; '
    'Дата: published; Ссылка: полный url из данных; '
    'Тема: одна из категорий «LLM-агенты и инструменты», '
    '«Безопасность агентов», «Публикация исследований». '
    'Обязательно включи полный URL каждой выбранной статьи. '
    'Используй только полученные записи. Не добавляй пересказ результатов, '
    'числовые показатели, число просмотренных или обещания эффективности. '
    'Если incomplete=true, начни с предупреждения, что часть записей пропущена фильтром.'
)
output = json.dumps(data, ensure_ascii=False)
error = _scan_cron_prompt(output)
if error:
    raise ValueError('Данные источника не прошли проверку Hermes')
Path(data['source_file']).with_name('model-source.json').write_text(output)
print(output)
