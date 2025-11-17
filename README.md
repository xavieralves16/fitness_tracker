# IronLog

IronLog is a Django-based powerlifting tracker that lets athletes log workouts, monitor personal records, and visualize progress across squat, bench press, deadlift, and accessory exercises. The app pairs a structured backend with interactive dashboards so lifters can see training volume trends, totals, and Wilks scores at a glance.

## Features
- **Workout logging:** Create workouts and record individual sets with weight, reps, distance, or duration.
- **Exercise library:** Start with predefined compound lifts and add custom accessory movements; remove personal entries when needed.
- **Personal records:** Automatically detect and store new PRs while reviewing workouts.
- **Progress dashboard:** Chart weekly/monthly volume, per-exercise volume share, PR timelines, and powerlifting totals with Wilks calculations.
- **Profile management:** Capture body metrics, training level, unit preference, and profile photos.
- **CSV exports:** Download workout histories and personal records for analysis or backups.

## Tech Stack
- **Backend:** Python 3, Django
- **Frontend:** Django templates, JavaScript, Chart.js (via static assets)
- **Database:** SQLite (default; configurable to PostgreSQL/MySQL)
- **Auth:** Django authentication (registration, login, logout)

## Project Structure
```
manage.py
fitness_project/         # Django project configuration
workouts/                # Core app (models, views, templates, static assets)
    models.py            # Profile, Exercise, Workout, WorkoutSet, PersonalRecord
    views.py             # Authentication, dashboards, exports, and CRUD flows
    forms.py             # Profile, exercise, workout, and set forms
    urls.py              # App routes
requirements.txt         # Python dependencies
```

## Getting Started
### Prerequisites
- Python 3.10+
- virtualenv (recommended)
- SQLite (bundled) or another Django-supported database

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/xavieralves16/fitness_tracker.git
   cd fitness_tracker
      ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser (optional but recommended)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Open the app** at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Configuration
- Update database settings or static/media paths in `fitness_project/settings.py` as needed.
- File uploads (e.g., profile pictures) require `MEDIA_ROOT` and `MEDIA_URL` to be configured when deploying.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` for production deployments.

## Running Tests
Execute the Django test suite:
```bash
python manage.py test
```

## Data Exports
- **Workouts:** `/export/workouts` streams workout histories with set details to CSV.
- **Personal records:** `/export/prs` downloads PR data (exercise, best weight, date).

## Roadmap Ideas
- Add gamification elements (badges/achievements).
- Integrate nutrition or wearable APIs for holistic tracking.
- Expand stats to IPF points or other federations.
- Ship a PWA-style mobile experience.

## Author
Built by Xavier Alves as a CS50W capstone project.
