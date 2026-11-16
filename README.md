# На полях

Hermes Agent для исследовательских задач. Задание 2 по курсу pyweb2025.

## Сервер

- Провайдер: AEZA.
- Тариф: CLTs-1.
- Регион: США.
- Стоимость: €5,93 в месяц.
- Система: Ubuntu 26.04.1 LTS.
- Ресурсы: 1 vCPU, 2 ГБ RAM, диск 30 ГБ.

## Базовая настройка

Для агента выделен пользователь `agent` без прав рута. Настроены вход по SSH-ключу и firewall, установлены обновления системы.

## Docker

На VPS используются Docker 29.9.3 и Docker Compose 5.7.1. Работа Docker проверена командой `docker run --rm hello-world`.

## Модель

Бесплатная `nvidia/nemotron-3.5-lightning:free` через OpenRouter. Контекст: 1 000 000 токенов. Лимит расходов ключа: $50 без автоматического сброса. Проверочный запрос выполнен успешно.

## Контейнер

Настройки запуска находятся в `compose.yaml`. Каталог `data/` подключается к `/opt/data` внутри контейнера: здесь Hermes хранит конфигурацию, память и навыки. Этот каталог и файл `.env` не попадают в Git.

На Mac проверен запуск Hermes 0.23.0:

```bash
docker compose run --rm hermes --version
```

Мастер настройки запускается командой `docker compose run --rm hermes setup`. Конфигурация сохраняется в `data/config.yaml`, ключи в `data/.env`.

Для запуска бота в фоне:

```bash
docker compose up -d
docker compose logs -f
```

Бот: [@gentofluck_margin_bot](https://t.me/gentofluck_margin_bot). Доступ разрешён только моему Telegram ID.
