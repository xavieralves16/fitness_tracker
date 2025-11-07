from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import User, Profile, Exercise, Workout, WorkoutSet
from django.db import IntegrityError
from .forms import ProfileForm, ExerciseForm, WorkoutForm, WorkoutSetForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "workouts/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "workouts/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "workouts/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "workouts/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "workouts/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "workouts/register.html")
    
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile) 
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "workouts/profile.html", {"form": form, "profile": profile})


@login_required
def exercise_library(request):
    """
    Display all exercises (default + user's custom ones) and allow adding new ones.
    """
    # Show all global (non-custom) exercises + user's custom ones
    exercises = Exercise.objects.filter(is_custom=False) | Exercise.objects.filter(user=request.user)

    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES) 
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.is_custom = True
            exercise.save()
            return redirect("exercises")
    else:
        form = ExerciseForm()

    return render(request, "workouts/exercises.html", {
        "form": form,
        "exercises": exercises,
    })


@login_required
def delete_exercise(request, exercise_id):
    """
    Allow a user to delete their own custom exercises.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user, is_custom=True)
    exercise.delete()
    return redirect("exercises")

@login_required
def workouts_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by("-date")
    return render(request, "workouts/workouts.html", {"workouts": workouts})


@login_required
def add_workout(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect("workout_detail", workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, "workouts/add_workout.html", {"form": form})


@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    sets = workout.sets.all().select_related("exercise")

    if request.method == "POST":
        form = WorkoutSetForm(request.POST)
        if form.is_valid():
            workout_set = form.save(commit=False)
            workout_set.workout = workout
            workout_set.save()
            return redirect("workout_detail", workout_id=workout.id)
    else:
        form = WorkoutSetForm()

    return render(request, "workouts/workout_detail.html", {
        "workout": workout,
        "sets": sets,
        "form": form,
    })
