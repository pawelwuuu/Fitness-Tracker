# 🏋️‍♂️ Fitness Tracker - Django + HTMX

**Fitness Tracker** is a web application for monitoring health and training progress. It allows users to:

- calculate BMI, BMR, and other indicators,
- keep a weight log,
- receive personalized dietary and training recommendations,
- browse guides and educational content,
- compare "before and after" photos,
- use ready-made workout plans.

---

## ⚙️ Tech Stack

### Backend:

- Python 3.10+
- Django 4+
- SQLite / PostgreSQL
- Django ORM
- Django Admin

### Frontend:

- HTMX – dynamic UI without JS frameworks
- Tailwind CSS (optional)
- Alpine.js (optional for simple interactions)

### Others:

- Pillow – for image handling
- Django Forms and Form Validation
- Responsive Design

---

## 📁 Project Structure

```
fitness_project/
├── manage.py
├── fitness_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tracker/
│   ├── migrations/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── weight.py
│   │   ├── nutrition.py
│   │   ├── training.py
│   │   └── photo.py
│   ├── views/
│   ├── urls.py
│   ├── templates/
│   │   └── tracker/
│   │       ├── base.html
│   │       └── ...
│   ├── static/
│   ├── forms.py
│   └── admin.py
```

---

## 🔧 Quick Start

⚠️ Note: for Tailwind to work you need to set the path to `npm`. See the bottom of this README.

```bash
git clone ...
cd fitness_tracker

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py tailwind install
python manage.py tailwind start
python manage.py runserver
```

## 🔧 Test User and Tips

Login: `testuser`  
Password: `Test1234`

```bash
python manage.py add_test_user
python manage.py populate_tips
```

It is also important to set the `NPM_BIN_PATH` in the root `settings.py` to point to your npm executable.

Example:

```bash
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
```
