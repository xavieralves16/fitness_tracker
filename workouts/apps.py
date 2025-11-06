from django.apps import AppConfig
from django.db.utils import OperationalError

class WorkoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workouts'

    def ready(self):
        """
        Preload default exercises (Squat, Bench Press, Deadlift)
        into the database when the app is ready.
        """
        from .models import Exercise  # import inside to avoid circular imports

        try:
            defaults = [
                ("Squat", "squat", "The classic powerlifting leg movement."),
                ("Bench Press", "bench", "Primary chest powerlifting movement."),
                ("Deadlift", "deadlift", "Fundamental posterior chain exercise."),
            ]
            for name, category, desc in defaults:
                Exercise.objects.get_or_create(
                    name=name,
                    category=category,
                    description=desc,
                    is_custom=False,
                    user=None,
                )
        except OperationalError:
            # happens on first migration (DB not ready)
            pass
