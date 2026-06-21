# TEAM_SER_X FEAR BOT

[![Python CI](https://github.com/SER-X-FEAR/TEAM_SER_X_FEAR_BOT/actions/workflows/python-ci.yml/badge.svg)](https://github.com/SER-X-FEAR/TEAM_SER_X_FEAR_BOT/actions/workflows/python-ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Highrise Bot для организации `SER-X-FEAR` — стартовый репозиторий для разработки игрового бота на Python, который будет взаимодействовать с Highrise API, отправлять уведомления, обрабатывать команды и автоматизировать задачи.

## Что уже настроено

- `README.md` с руководством по запуску
- `requirements.txt` и `pyproject.toml`
- `.env.example` для переменных окружения
- `src/main.py` — точка входа бота
- GitHub Actions для проверки синтаксиса
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- шаблоны issue и pull request
- `CODEOWNERS` для контроля изменений
- лицензия MIT

## Требования

- Python 3.11+
- `pip`

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SER-X-FEAR/TEAM_SER_X_FEAR_BOT.git
   cd TEAM_SER_X_FEAR_BOT
   ```
2. Установите зависимости:
   ```bash
   python -m pip install -U pip
   python -m pip install -r requirements.txt
   ```
3. Скопируйте `.env.example` в `.env` и заполните значения:
   - на Windows:
     ```powershell
     copy .env.example .env
     ```
   - на Linux/macOS:
     ```bash
     cp .env.example .env
     ```

## Установка пакета

1. Установите пакет в editable режиме для разработки:
   ```bash
   python -m pip install -e .
   ```

## Запуск пакета

1. Запустите бота через пакет:
   ```bash
   python -m team_ser_x_fear_bot
   ```

## Кроссплатформенность

Проект разработан для работы на Windows, macOS и Linux. CI проверяет сборку и запуск на всех трёх платформах.

## Переменные окружения

- `BOT_TOKEN` — токен для бота
- `HIGHRISE_API_URL` — адрес API Highrise
- `NODE_ENV` — режим (например, `development`)

## Запуск

Запустите бота командой:
```bash
python src/main.py
```

## Разработка

- Все изменения вносятся через pull request.
- Для исправлений и новых функций создавайте отдельные ветки, например:
  - `feature/имя`
  - `bugfix/имя`
  - `docs/имя`
- Перед отправкой PR проверьте синтаксис:
  ```bash
  python -m compileall src
  ```

## Команда и вклад

Для участия см. `CONTRIBUTING.md`.

Если вы хотите предложить новую функцию или найти баг, используйте шаблоны:
- `Bug report`
- `Feature request`

## Политика проекта

- Репозиторий открыт для организации `SER-X-FEAR`.
- Все изменения проходят через Pull Request.
- Ветка `master` защищена и требует прохождения CI.

## Лицензия

Этот проект лицензирован по MIT. См. `LICENSE`.
