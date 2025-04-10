from django.urls import path, include
from rest_framework.routers import DefaultRouter

from auth_app import views

router = DefaultRouter()

router.register('register', viewset=views.RegisterPatientView, basename='register')
router.register('patient', viewset=views.PatientView, basename='patient')
router.register('login', viewset=views.LoginView, basename='login')
router.register('logout', viewset=views.LogoutView, basename='logout')
router.register('acte_mariage', viewset=views.ActeMariageView, basename='acte_mariage')
router.register('acte_naissance', viewset=views.ActeNaissanceView, basename='acte_naissance')
router.register('contact_urgence', viewset=views.ContactUrgenceView, basename='contact_urgence')
router.register('antecedent', viewset=views.AntecedentView, basename='antecedent')
router.register('allergie', viewset=views.AllergieView, basename='allergie')

urlpatterns = [
    path('', include(router.urls)),
]