from django import forms
from .models import Profile, Exercise, WorkoutSet, Workout

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "age", "height", "weight", "preferred_units", "level"]
        widgets = {
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "height": forms.NumberInput(attrs={"class": "form-control", "step": "0.1"}),
            "weight": forms.NumberInput(attrs={"class": "form-control", "step": "0.1"}),
            "preferred_units": forms.Select(attrs={"class": "form-control"}),
            "level": forms.Select(attrs={"class": "form-control"}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "category", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["notes"]
        widgets = {
            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Optional notes about this workout..."
            }),
        }


class WorkoutSetForm(forms.ModelForm):
    """
    Formulário para adicionar sets (exercício, repetições, peso) a um Workout.
    """
    class Meta:
        model = WorkoutSet
        fields = ["exercise", "repetitions", "weight"]
        widgets = {
            "exercise": forms.Select(attrs={"class": "form-control"}),
            "repetitions": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1
            }),
            "weight": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.5",
                "min": 0
            }),
        }