from ninja import NinjaAPI
from auth_app.models import *
from .schemas import *
app1=NinjaAPI(version="2.2.3",urls_namespace="auth_app_allergies")
@app1.get("allergies/",response=list[SchemaAllergie])
def get_allergie(request):
    return Allergie.objects.all()
@app1.get("alergie/{id}",response=SchemaAllergie)
def GetAllergieById(request ,id:int):
    allg=Allergie.objects.get(id=id)
    return allg
@app1.post("AddAlergie/",response=SchemaAllergie)
def AddAllergie(request,allg:SchemaCreateAllergie):
    allergie_data=allg.model_dump()
    allergie=Allergie.objects.create(**allergie_data)
    return allergie

@app1.delete("DeleteAlergie/{id}",response=SchemaAllergie)
def DeleteAlergie(request,id:int):
    allg=Allergie.objects.get(id=id)
    allg.delete()
    return {"success":True,"message":"alergie suprimer avec succes"}
    
@app1.put("UpdateAllergie/{id}",response=SchemaAllergie)
def UpdateAllergie(request,id:int,allg:SchemaCreateAllergie):
    allergie=Allergie.objects.get(id=id)
    for atb ,value in allg.model_dump().items():
       
       setattr(allergie,atb,value)
    allergie.save()   
    return allergie
       