# Powerlifting Tracker

A web application built with **Django** and **JavaScript** for powerlifters to log workouts, track personal records (PRs), and monitor progress over time.  
The application focuses specifically on **squat, bench press, and deadlift**, while also supporting accessory exercises.  
It includes **BMI calculation, PR tracking, and powerlifting total (SBD)**, with charts to visualize performance.

---

## Distinctiveness and Complexity

This project is distinct from other CS50W assignments for several reasons:

- Unlike the e-commerce or social network projects, this application is **specialized and domain-specific** (powerlifting).  
- It requires **custom models** for workouts, exercises, sets, and personal records, with multiple relationships between them.  
- The application includes **real-world performance metrics** such as BMI, total (squat + bench + deadlift), and Wilks score (strength relative to bodyweight).  
- A dynamic **dashboard with interactive charts** (using Chart.js/JavaScript) provides users with progress visualization.  
- The project combines **backend logic (Django models and queries)** with **frontend interactivity (JavaScript, AJAX, charts)** to deliver a complex and feature-rich experience.  

This ensures that the project is both **unique** in scope and **complex enough** to showcase advanced web development skills.

---

## Features (Planned / Implemented)

- [ ] User registration and authentication  
- [ ] Profile management with unit system selection (metric/imperial)  
- [ ] Exercise library (preloaded with squat, bench, deadlift; user can add custom exercises)  
- [ ] Log workouts with sets (reps, weight, duration, distance)  
- [ ] Automatic calculation of training volume (weight × reps)  
- [ ] Personal Record (PR) tracking for each exercise  
- [ ] Dashboard with:
  - Progression charts for squat, bench, and deadlift  
  - Weekly/monthly training volume  
  - Powerlifting total (SBD) and Wilks score  
- [ ] Export workout history to CSV  

---

## File Structure (planned)

fitness_project/        # Main Django project folder  
│  
├── workouts/           # Core app  
│   ├── models.py       # Profile, Exercise, Workout, WorkoutSet, PersonalRecord  
│   ├── views.py        # Views for workouts, dashboard, PRs  
│   ├── urls.py         # App routes  
│   ├── templates/      # HTML templates  
│   ├── static/         # CSS/JS  
│  
├── fitness_project/    # Project configuration  
│   ├── settings.py  
│   ├── urls.py  
│  
├── requirements.txt    # Python dependencies  
├── README.md           # Project documentation  
└── .gitignore  

---

## Installation and Setup

1. Clone this repository:  
   git clone https://github.com/xavieralves16/fitness_tracker.git)
   cd fitness_tracker

2. Create and activate a virtual environment:  
   python3 -m venv venv  
   source venv/bin/activate    # On macOS/Linux  
   venv\Scripts\activate       # On Windows  

3. Install dependencies:  
   pip install -r requirements.txt  

4. Run migrations:  
   python manage.py makemigrations  
   python manage.py migrate  

5. Create a superuser:  
   python manage.py createsuperuser  

6. Start the development server:  
   python manage.py runserver  

7. Visit the app at http://127.0.0.1:8000/  

---

## Screenshots / Demo (to be added)

- [ ] Dashboard view  
- [ ] Workout logging page  
- [ ] PR tracking example  

---

## Future Improvements

- Add gamification (badges for milestones)  
- Integration with APIs (e.g., nutrition or fitness devices)  
- Advanced statistics (IPF points calculation)  
- Mobile PWA support  

---

## Author

Developed by Xavier Alves.  
Capstone project for **CS50’s Web Programming with Python and JavaScript (CS50W)**.  

---
