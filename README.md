# EduLinguaUz — Full A1 (4 languages) MVP

## Quick start
```
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/seed.json
python manage.py runserver
```
Key endpoints:
- GET /api/languages/
- GET /api/lessons/by?lang=es&level=A1
- GET /api/stories/by?lang=es&level=A1
- GET /api/search/?q=hello
- POST /api/certificate/ -> returns PDF

Open `frontend/index.html`. If backend is on another host, set `API_BASE` accordingly.