from ninja import  Schema,ModelSchema
from auth_app.models import *
from consultation.models import *
class SchemaAllergie(ModelSchema):
    class Meta:
        model=Allergie

        fields=('id','allergene','symptomes','gravite','traitement')
class SchemaCreateAllergie(Schema):
    allergene:str
    symptomes:str     
    traitement:str
    gravite:str  
#schemas pour vaccinations
class SchemaVaccinations(ModelSchema):
    class Meta:
        model=Vaccination

        fields=('id','nom','type')
class SchemaCreateVaccinations(Schema):
    nom:str
    type:str     
   
        
     