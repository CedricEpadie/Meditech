from ninja import NinjaAPI, Router 
from auth_app.models import *
from .schemas import *
from consultation.models import *




app1 = Router()

@app1.get("allergies/", response=list[SchemaAllergie])
def get_allergie(request):
    return Allergie.objects.all()

@app1.get("alergie/{id}", response=SchemaAllergie)
def get_allergie_by_id(request, id: int):
    allergie = Allergie.objects.get(id=id)
    return allergie

@app1.post("AddAlergie/", response=SchemaAllergie)
def add_allergie(request, allg: SchemaCreateAllergie):
    allergie_data = allg.model_dump()
    allergie = Allergie.objects.create(**allergie_data)
    return allergie

@app1.delete("DeleteAlergie/{id}", response=dict)
def delete_allergie(request, id: int):
    allergie = Allergie.objects.get(id=id)
    allergie.delete()
    return {"success": True, "message": "Allergie supprimée avec succès"}

@app1.put("UpdateAllergie/{id}", response=SchemaAllergie)
def update_allergie(request, id: int, allg: SchemaCreateAllergie):
    allergie = Allergie.objects.get(id=id)
    for atb, value in allg.model_dump().items():
        setattr(allergie, atb, value)
    allergie.save()
    return allergie


# route pour le module consultation

vaccination =Router()

from ninja import Router
from fastapi import HTTPException  # Importer HTTPException depuis FastAPI

vaccination = Router()



@vaccination.get("Vaccinations/", response=list[SchemaVaccinations])
def get_Vaccinations(request):
    try:
        return Vaccination.objects.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des vaccinations: {str(e)}")

@vaccination.get("Vaccination/{id}", response=SchemaVaccinations)
def GetVaccinationById(request, id: int):
    try:
        return Vaccination.objects.get(id=id)
    except Vaccination.DoesNotExist:
        raise HTTPException(status_code=404, detail="Vaccination non trouvée")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération de la vaccination: {str(e)}")

@vaccination.post("AddVaccination/", response=SchemaVaccinations)
def AddVaccination(request, vacc: SchemaCreateVaccinations):
    try:
        Vaccination_data = vacc.model_dump()
        vaccination = Vaccination.objects.create(**Vaccination_data)
        return vaccination
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de la vaccination: {str(e)}")

@vaccination.delete("DeleteVaccination/{id}", response=SchemaVaccinations)
def DeleteVaccination(request, id: int):
    try:
        vaccination = Vaccination.objects.get(id=id)
        vaccination.delete()
        return {"success": True, "message": "Vaccination supprimée avec succès"}
    except Vaccination.DoesNotExist:
        raise HTTPException(status_code=404, detail="Vaccination non trouvée")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la suppression de la vaccination: {str(e)}")

@vaccination.put("UpdateVaccination/{id}", response=SchemaVaccinations)
def UpdateVaccination(request, id: int, vacc: SchemaCreateVaccinations):
    try:
        vaccination = Vaccination.objects.get(id=id)
        for atb, value in vacc.model_dump().items():
            setattr(vaccination, atb, value)
        vaccination.save()
        return vaccination
    except Vaccination.DoesNotExist:
        raise HTTPException(status_code=404, detail="Vaccination non trouvée")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la mise à jour de la vaccination: {str(e)}")