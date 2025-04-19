from django.contrib import admin
from .models import *
@admin.register(ActeNaissance)
class ActeNaissanceAdmin(admin.ModelAdmin):
    list_display = ('nom_enfant', 'sexe', 'date_dressage')
    search_fields = ('nom_enfant', 'nom_pere', 'nom_mere')

@admin.register(Allergie)
class AllergieAdmin(admin.ModelAdmin):
    list_display = ('allergene', 'gravite')
    search_fields = ('allergene',)

@admin.register(ActeMariage)
class ActeMariageAdmin(admin.ModelAdmin):
    list_display = ('nom_personne',)
    search_fields = ('nom_personne',)

@admin.register(Antecedent)
class AntecedentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'date_diagnostic')
    search_fields = ('nom',)

@admin.register(ContactUrgence)
class ContactUrgenceAdmin(admin.ModelAdmin):
    list_display = ('nom_contact', 'telephone')
    search_fields = ('nom_contact',)

@admin.register(Commissariat)
class CommissariatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lieu')
    search_fields = ('nom',)

@admin.register(Hopital)
class HopitalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lieu')
    search_fields = ('nom',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'type')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('patient', 'specialite')
    search_fields = ('patient__email',)

@admin.register(Policier)
class PolicierAdmin(admin.ModelAdmin):
    list_display = ('patient', 'commissariat')
    search_fields = ('patient__email',)
