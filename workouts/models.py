from django.contrib.auth.models import User
from django.db import models


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Extension of the User model for powerlifting tracking.
    Always stores data internally in metric (kg, cm).
    """
    UNIT_CHOICES = [
        ("metric", "Metric (kg, cm)"),
        ("imperial", "Imperial (lbs, ft/in)"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # stored in cm
    weight = models.FloatField(null=True, blank=True)  # stored in kg
    preferred_units = models.CharField(
        max_length=10, choices=UNIT_CHOICES, default="metric"
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")

    def __str__(self):
        return self.user.username

    # ----- Conversion Helpers -----
    def weight_in_lbs(self):
        """Returns bodyweight in pounds."""
        if self.weight:
            return round(self.weight * 2.20462, 2)
        return None

    def height_in_feet(self):
        """Returns height as (feet, inches)."""
        if self.height:
            total_inches = self.height / 2.54
            feet = int(total_inches // 12)
            inches = round(total_inches % 12)
            return f"{feet}′{inches}″"
        return None

    @property
    def bmi(self):
        """BMI is always calculated using metric (kg/m²)."""
        if self.height and self.weight:
            return round(self.weight / ((self.height / 100) ** 2), 2)
        return None


class Exercise(models.Model):
    """
    Exercise library: includes main powerlifting lifts and accessories.
    """
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ("squat", "Squat"),
            ("bench", "Bench"),
            ("deadlift", "Deadlift"),
            ("accessory", "Accessory"),
        ]
    )
    description = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(default=False)  # whether created by the user

    def __str__(self):
        return self.name


class Workout(models.Model):
    """
    A workout session belonging to a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

    @property
    def total_volume(self):
        """
        Calculate the total volume of the workout:
        sum of (weight * reps) for all sets.
        """
        return sum([s.volume for s in self.sets.all()])


class WorkoutSet(models.Model):
    """
    A single set performed in a workout, linked to an exercise.
    Can represent strength sets or other types (cardio, accessory).
    """
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="sets")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)   # kg (strength training)
    duration = models.IntegerField(null=True, blank=True)  # seconds (cardio/HIIT)
    distance = models.FloatField(null=True, blank=True)    # km (running/biking)

    def __str__(self):
        return f"{self.exercise.name} - {self.repetitions or 0} reps"

    @property
    def volume(self):
        """
        Volume of the set (weight * reps).
        Returns 0 if missing.
        """
        if self.weight and self.repetitions:
            return self.weight * self.repetitions
        return 0


class PersonalRecord(models.Model):
    """
    Stores 1-rep max (PR) records for each exercise.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name}: {self.weight}kg"


# ----- Signals -----
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a profile when a new user is created."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Ensure profile is saved whenever the user is saved."""
    instance.profile.save()
