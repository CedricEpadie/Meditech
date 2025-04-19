from ninja import  Schema,ModelSchema
from auth_app.models import *
class SchemaAllergie(ModelSchema):
    class Meta:
        model=Allergie

        fields=('id','allergene','symptomes','gravite','traitement')
class SchemaCreateAllergie(Schema):
    allergene:str
    symptomes:str     
    traitement:str
    gravite:str  
    
        
     