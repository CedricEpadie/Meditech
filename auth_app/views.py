from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import status
from auth_app import serializers, models

from django.contrib.auth import login, logout
from .backends import EmailBackend

class RegisterPatientView(viewsets.ModelViewSet):
    serializer_class = serializers.RegisterPatientSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()
            patient.set_password(patient.password)
            patient.save()
            if patient.type == 'Medecin':
                models.Medecin.objects.create(patient=patient)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif patient.type == 'Policier':
                models.Policier.objects.create(patient=patient)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientView(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all()
    http_method_names = ['get', 'delete', 'patch']
    
class LoginView(viewsets.ModelViewSet):
    serializer_class = serializers.LoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        patient = EmailBackend().authenticate(request, email=email, password=password)
        
        if patient is not None:
            login(request, patient)
            patient_serializer = serializers.PatientSerializer(patient)
            return Response(patient_serializer.data, status=status.HTTP_200_OK)
        
        return Response({'error': 'email ou mot de passe incorrect'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(viewsets.ModelViewSet):
    serializer_class = serializers.LogoutSerializer 
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response({'message': 'deconnexion reussie'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'erreur lors de la deconnexion'}, status=status.HTTP_400_BAD_REQUEST)
     
class ActeMariageView(viewsets.ModelViewSet):
    serializer_class = serializers.ActeMariageSerializer
    queryset = models.ActeMariage.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = models.Patient.objects.get(id=request.user.id)
            if patient.acte_mariage is None:
                acte_mariage = serializer.save()
                patient.acte_mariage = acte_mariage
                patient.save()
            else:
                return Response({'error': 'l\'utilisateur a déjà ajouter un acte de mariage'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ActeNaissanceView(viewsets.ModelViewSet):
    serializer_class = serializers.ActeNaissanceSerialier
    queryset = models.ActeNaissance.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = models.Patient.objects.get(id=request.user.id)
            if patient.acte_naissance is None:
                acte_naissance = serializer.save()
                patient.acte_naissance = acte_naissance
                patient.save()
            else:
                return Response({'error': 'l\'utilisateur a déjà ajouter un acte de mariage'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactUrgenceView(viewsets.ModelViewSet):
    serializer_class = serializers.ContactUrgenceSerializer
    queryset = models.ContactUrgence.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    
    def list(self, request, *args, **kwargs):
        patient = request.user
        contact_urgence = patient.contacts_urgence.all()
        contact_urgence_serialize = self.serializer_class(contact_urgence, many=True)
        
        return Response(contact_urgence_serialize.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            contact_urgence = serializer.save()
            patient = request.user
            patient.contacts_urgence.add(contact_urgence)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AntecedentView(viewsets.ModelViewSet):
    serializer_class = serializers.AntecedentSerializer
    queryset = models.Antecedent.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    
    def list(self, request, *args, **kwargs):
        patient = request.user
        antecedent = patient.antecedents.all()
        antecedent_serializer = self.serializer_class(antecedent, many=True)
        
        return Response(antecedent_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            antecedent = serializer.save()
            patient = request.user
            patient.antecedents.add(antecedent)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllergieView(viewsets.ModelViewSet):
    serializer_class = serializers.AllergieSerializer
    queryset = models.Allergie.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'patch', 'delete']
    
    def list(self, request, *args, **kwargs):
        patient = request.user
        allergie = patient.allergies.all()
        allergie_serializer = self.serializer_class(allergie, many=True)
        
        return Response(allergie_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            allergie = serializer.save()
            patient = request.user
            patient.allergies.add(allergie)

            return Response(serializer.data, status=status.HTTP_201_CREATED)