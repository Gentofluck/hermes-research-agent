# Проверки настройки

## Запуск

Фрагмент журнала запуска контейнера:

```text
Syncing bundled skills into ~/.hermes/skills/ ...
Done: 0 new, 0 updated, 44 unchanged. 44 total bundled.
2026-11-17 23:04:02,737 WARNING agent.auxiliary_unavailable: Auxiliary Nous client unavailable: Nous Portal runtime credentials unavailable: Hermes is not logged into Nous Portal. Run `hermes model` to re-authenticate. (code: nous_auth_missing)
2026-11-17 23:04:13,078 WARNING hermes_plugins.platforms__telegram.adapter: [Telegram] Connected to Telegram (polling mode)
```

## Ответ бота

Запись о проверке на VPS 16 ноября. Данные чата скрыты; time обозначает обработку внутри Hermes.

```text
2026-11-16 22:52:00,659 INFO gateway.run: response ready: platform=telegram chat=[hidden] session=agent:main:telegram:dm:[hidden] time=1.0s api_calls=1 response=71 chars
```

## Память

Вопрос:

> Какие три критерия выбраны для сравнения методов в моей исследовательской задаче? Как поступать, если данных для сравнения нет? Ответь кратко.

Ответ агента:

> Критерии: время выполнения задачи, число ошибок пользователя, понятность интерфейса.
>
> Если данных для сравнения нет, прямо об этом сказывайте — не придумывайте результаты и ссылки на исследования.

## Вызов навыка

Запрос:

> Выполни paper-digest за последние 7 суток. Верни результат сценария без изменения.

Агент выполнил команду:

```bash
/opt/hermes/.venv/bin/python /opt/data/skills/research/paper-digest/scripts/digest.py
```

Ответ:

```text
Проверка arXiv: получено 0, отобрано 0.

За выбранный период подходящих работ в полученной выдаче не найдено.

Запрос: cat:cs.HC AND (ti:web OR ti:browser OR abs:web OR abs:browser) AND (ti:"adaptive interface" OR ti:"adaptive UI" OR ti:"personalization" OR ti:"user modeling" OR ti:"behavior-based adaptation" OR ti:"interface adaptation" OR abs:"adaptive interface" OR abs:"adaptive UI" OR abs:"personalization" OR abs:"user modeling" OR abs:"behavior-based adaptation" OR abs:"interface adaptation") AND (ti:"rule-based" OR ti:"machine learning" OR ti:"hybrid" OR abs:"rule-based" OR abs:"machine learning" OR abs:"hybrid")
Период: 7 суток.
```

## Расписание

Ежедневный запуск настроен на 09:00 МСК: `0 9 * * *`, часовой пояс `Europe/Moscow`. Запускается `paper-digest/scripts/digest.py` через `/opt/hermes/.venv/bin/python` в режиме `--no-agent`.
