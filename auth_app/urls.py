from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consultation.api import app1

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
router.register('face_register', viewset=views.FaceRegisterView, basename='face_register')
router.register('face_login', viewset=views.FaceLoginView, basename='face_login')

urlpatterns = [
    path('', include(router.urls)),
    path("api/",app1.urls),
    path('csrf/', views.get_csrf),
    
]