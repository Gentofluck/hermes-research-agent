# На полях

Hermes Agent в Docker для задания 2 курса pyweb2025. Бот получает новые статьи arXiv и составляет дайджест по смыслу аннотаций. Модель — бесплатная NVIDIA Nemotron через OpenRouter.

## Запуск

```sh
cp .env.example .env
bash scripts/setup.sh
bash scripts/seed.sh
docker compose up -d
```

В `.env` задаются каталог данных и UID/GID пользователя. На VPS используются `/home/agent/hermes-data` и `1000:1000`. Мастер сохраняет ключ OpenRouter, токен Telegram и разрешённый ID в каталог данных, подключённый как `/opt/data`.

До запуска нужно установить лимит расходов у провайдера. Ключи и токены хранятся вне Git. Агенту не подключаются папки других проектов и Docker socket. В чате он может выполнять команды внутри контейнера; в заданиях cron инструменты модели отключены, сбор данных выполняет подготовленный скрипт.

Темы и запросы arXiv заданы в `seed/memories/MEMORY.md`. Для ежедневного дайджеста:

```sh
docker compose exec hermes-agent hermes cron create '0 9 * * *' 'paper-digest: составь дайджест по приложенным данным на русском' --skill paper-digest --script paper-digest-source.py --deliver telegram --timezone Europe/Moscow --reasoning-effort none --pin
```

[Отчёт](report/report.md) · [T1: сравнение платформ](report/T1.md) · [Навык](seed/skills/research/paper-digest/SKILL.md)

Код и навык распространяются по [MIT](LICENSE).
