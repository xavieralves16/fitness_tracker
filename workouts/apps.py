from django.apps import AppConfig
from django.db.utils import OperationalError

class WorkoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workouts'

    def ready(self):
        """
        Preload default exercises (Back Squat, Spoto Bench Press, Deficit Deadlift)
        and link each to its static GIF.
        """
        from .models import Exercise
        try:
            defaults = [
                {
                    "name": "Back Squat",
                    "category": "squat",
                    "description": "The classic barbell back squat targeting legs and core.",
                    "image": "workouts/images/BB_BSQT.gif",
                },
                {
                    "name": "Spoto Bench Press",
                    "category": "bench",
                    "description": "Paused bench variation emphasizing control and stability.",
                    "image": "workouts/images/SPOTO_BP.gif",
                },
                {
                    "name": "Deficit Deadlift",
                    "category": "deadlift",
                    "description": "Deadlift performed from a small platform to increase range of motion.",
                    "image": "workouts/images/DEFICIT_DL.gif",
                },
            ]

            for data in defaults:
                Exercise.objects.get_or_create(
                    name=data["name"],
                    category=data["category"],
                    description=data["description"],
                    is_custom=False,
                    user=None
                )

        except OperationalError:
            # Happens during first migration
            pass
