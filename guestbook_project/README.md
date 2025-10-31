# Django Guestbook (SQLite)

Conversión de la app Flask a Django usando el mismo CSS y SQLite como base de datos.

## Estructura
- Proyecto: `guestbook_project`
- App: `guestbook`
- Modelo: `Entry(content, created_at)`

## Puesta en marcha

```bash
cd guestbook_project
python -m venv .venv
source .venv/bin/activate  # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Abre http://localhost:8000/

## Administración
```bash
python manage.py createsuperuser
```
