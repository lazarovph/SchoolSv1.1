# SchoolSv1.1

Онлайн платформа за управление на домашни работи, задачи, тестове и ученически профили.

## Структура
- Flask + SQLite
- Модулна структура с Blueprints: `admin`, `auth`, `main`, `tasks`
- Bootstrap за базов интерфейс

## Стартиране

```bash
git clone https://github.com/lazarovph/SchoolSv1.1.git
cd SchoolSv1.1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
