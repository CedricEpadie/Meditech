from django.db import models
class Vaccination(models.Model):
    type=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    def __str__(self):
        return f" vaccin {self.nom}"