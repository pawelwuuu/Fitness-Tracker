# 🏋️‍♂️ Fitness Tracker - Django + HTMX

**Fitness Tracker** to aplikacja webowa do monitorowania zdrowia i progresu treningowego. Pozwala użytkownikom na:

- obliczanie BMI, BMR i innych wskaźników,
- prowadzenie dziennika wagi,
- otrzymywanie zindywidualizowanych zaleceń dietetycznych i treningowych,
- przeglądanie porad i edukatorów,
- porównywanie zdjęć „przed i po”,
- korzystanie z gotowych planów treningowych.

---

## ⚙️ Stack technologiczny

### Backend:

- Python 3.10+
- Django 4+
- SQLite / PostgreSQL
- Django ORM
- Django Admin

### Frontend:

- HTMX – dynamiczne UI bez frameworków JS
- Tailwind CSS (opcjonalnie)
- Alpine.js (opcjonalnie dla prostych interakcji)

### Inne:

- Pillow – do obsługi zdjęć
- Django Forms i Form Validation
- Responsive Design

---

## 📁 Struktura projektu

fitness_project/  
├── manage.py  
├── fitness_project/  
│ ├── **init**.py  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
├── tracker/  
│ ├── migrations/  
│ ├── models/  
│ │ ├── **init**.py  
│ │ ├── user.py  
│ │ ├── weight.py  
│ │ ├── nutrition.py  
│ │ ├── training.py  
│ │ └── photo.py  
│ ├── views/
│ ├── urls.py  
│ ├── templates/  
│ │ └── tracker/  
│ │ ├── base.html  
│ │ └── ...  
│ ├── static/  
│ ├── forms.py  
│ └── admin.py

---

## 🔧 Szybki start

```bash
git clone ...
cd fitness_tracker

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Również ważne jest aby w root settings.py ustawic linijke NPM_BIN_PATH tak aby wskazywala na npm

Przykład

```bash
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
```
