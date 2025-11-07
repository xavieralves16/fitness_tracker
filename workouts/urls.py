from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile_view, name='profile'),
    path('exercises', views.exercise_library, name='exercises'),
    path('exercises/delete/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
    path("workouts", views.workouts_list, name="workouts_list"),
    path("workouts/add", views.add_workout, name="add_workout"),
    path("workouts/<int:workout_id>/", views.workout_detail, name="workout_detail"),
    path("prs", views.personal_records, name="personal_records"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("export/workouts", views.export_workouts_csv, name="export_workouts_csv"),
    path("export/prs", views.export_prs_csv, name="export_prs_csv"),
]