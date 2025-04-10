from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class ActeNaissance(models.Model):
    SEXE_CHOICE = [
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin')
    ]
    
    nom_enfant = models.CharField(max_length=50)
    lieux_naissance = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50, choices=SEXE_CHOICE)
    nom_pere = models.CharField(max_length=50)
    lieu_naissance_pere = models.CharField(max_length=50)
    lieu_habitat_pere = models.CharField(max_length=50)
    profession_pere = models.CharField(max_length=50)
    nom_mere = models.CharField(max_length=50)
    lieu_naissance_mere = models.CharField(max_length=50)
    lieu_habitat_mere = models.CharField(max_length=50)
    date_dressage = models.DateField()
    
    def __str__(self):
        return f"Acte de {self.nom_enfant}"
    
class Allergie(models.Model):
    allergene = models.CharField(max_length=50)
    symptomes = models.TextField()
    gravite = models.CharField(max_length=50)
    traitement = models.TextField()
    
    def __str__(self):
        return self.allergene
    
class ActeMariage(models.Model):
    nom_personne = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Acte de {self.nom_personne}"

class Antecedent(models.Model):
    nom = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    date_diagnostic = models.DateField()
    traitement = models.CharField(max_length=50)
    
class ContactUrgence(models.Model):
    nom_contact = models.CharField(max_length=50)
    lien = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    
class Commissariat(models.Model):
    nom = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom

class Hopital(models.Model):
    nom = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
class PatientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Patient(AbstractUser):
    GROUPE_SANGUIN_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]

    RHESUS_CHOICES = [
        ('+', 'Positif'),
        ('-', 'Négatif'),
    ]
    
    TYPE_CHOICES = [
        ('Patient', 'Patient'),
        ('Medecin', 'Medecin'),
        ('Policier', 'Policier')
    ]
    
    username = None
    email = models.CharField(max_length=250, unique=True)
    groupe_sanguin = models.CharField(max_length=2, choices=GROUPE_SANGUIN_CHOICES)
    rhesus = models.CharField(max_length=1, choices=RHESUS_CHOICES)
    face_encoding = models.TextField(blank=True, null=True, help_text="Encodage pour la reconnaissance faciale")
    acte_mariage = models.OneToOneField(ActeMariage, on_delete=models.SET_NULL, null=True, blank=True)
    acte_naissance = models.OneToOneField(ActeNaissance, on_delete=models.SET_NULL, null=True, blank=True)
    allergies = models.ManyToManyField(Allergie, blank=True)
    antecedents = models.ManyToManyField(Antecedent, blank=True)
    contacts_urgence = models.ManyToManyField(ContactUrgence, blank=True)

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = PatientManager()
    
    def __str__(self):
        return self.get_full_name()
    
class Medecin(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=50, blank=True, null=True)
    hopitaux = models.ForeignKey(Hopital, on_delete=models.CASCADE, blank=True, null=True)
    
class Policier(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE, blank=True, null=True)