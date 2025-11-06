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
]