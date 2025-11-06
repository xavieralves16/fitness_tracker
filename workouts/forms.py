from django import forms
from .models import Profile, Exercise

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
        fields = ["name", "category", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }