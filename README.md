# Niraj Kumar Sharma — Portfolio

Cyberpunk-themed personal portfolio website built with **Django**, **HTML**, **CSS**, and **JavaScript**.

---

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── db.sqlite3               (auto-created after migrations)
│
├── portfolio/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── core/                    # Portfolio app
    ├── models.py            # Project, Skill, ContactMessage
    ├── views.py             # index view + AJAX contact handler
    ├── forms.py             # ContactForm (ModelForm)
    ├── urls.py              # app URLs
    ├── admin.py             # Admin panel config
    │
    ├── templates/core/
    │   └── index.html       # Main portfolio template
    │
    └── static/core/
        ├── css/
        │   └── style.css    # All styles
        ├── js/
        │   ├── animations.js  # Cursor, particles, counters, skill bars
        │   └── main.js        # Terminal, nav, contact form AJAX
        └── images/
            └── niraj.jpg    # Profile photo
```

---

## Setup & Run

```bash
# 1. Clone / unzip the project
cd portfolio

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin user (to manage projects via /admin)
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## Admin Panel

Visit **http://127.0.0.1:8000/admin** to:
- Add / edit **Projects** (will replace the hardcoded ones)
- Add / edit **Skills** (tech stack cards)
- View **Contact Messages** sent through the form

---

## Contact Form Email (Production)

In `portfolio/settings.py`, change:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

---

## Deployment (basic)

```bash
# Collect static files
python manage.py collectstatic

# Set in settings.py for production:
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'use-a-real-random-key'
```
