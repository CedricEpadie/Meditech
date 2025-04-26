from django.contrib import admin
from django.urls import path, include, re_path
from consultation.api  import  *

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ninja  import NinjaAPI
api = NinjaAPI()
api.add_router("/allergie/", app1)
api.add_router("/vaccination/",vaccination)

urlpatterns = [
    path('admin/', admin.site.urls),
]

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Documentation interactive de votre API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@votreapp.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path("api/",api.urls),
   
    

    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc (optionnel, autre UI)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
