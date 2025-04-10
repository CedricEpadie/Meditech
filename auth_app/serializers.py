from rest_framework import serializers
from auth_app import models

class ActeNaissanceSerialier(serializers.ModelSerializer):
    class Meta:
        model = models.ActeNaissance
        fields = '__all__'

class ActeMariageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActeMariage
        fields = '__all__'
        
class AllergieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Allergie
        fields = '__all__'
        
class AntecedentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Antecedent
        fields = '__all__'
        
class ContactUrgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUrgence
        fields = '__all__'

class RegisterPatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.Patient
        fields = ['email', 'password', 'first_name', 'last_name', 'groupe_sanguin', 'rhesus', 'type']
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['email', 'password']
        
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = []

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['id', 'email', 'first_name', 'last_name', 'groupe_sanguin', 'rhesus', 'acte_mariage', 'acte_naissance', 'allergies', 'antecedents', 'contacts_urgence', 'type']

class ContactUrgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUrgence
        fields = ['id', 'nom_contact', 'lien', 'telephone']
        
class AntecedentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Antecedent
        fields = ['id', 'type', 'date_diagnostic', 'traitement']
        
class AllergieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Allergie
        fields = ['id', 'allergene', 'symptomes', 'gravite', 'traitement']