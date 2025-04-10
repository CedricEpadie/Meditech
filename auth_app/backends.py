from django.contrib.auth.backends import ModelBackend
from .models import Patient

# Definition du noveau model backend pour l'authentification (On utilise l'email)
class EmailBackend(ModelBackend):
    def authenticate(self, request, email = None, password = None, **kwargs):
        try:
            user = Patient.objects.get(email=email)
            if user.check_password(password):
                return user
        except Patient.DoesNotExist:
            return None