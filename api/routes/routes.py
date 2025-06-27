from fastapi import APIRouter, HTTPException
from api.schemas import PredictionRequest, DynamicPredictionRequest
from api.services.model_services import ModelService

router = APIRouter(
    prefix="/models",
    tags=["models"]
)

model_services = ModelService()

@router.post("/predict/lille", summary="Estime le prix au m² à Lille")
async def predict_lille(request: PredictionRequest):
    return model_services.get_predict_lille(request)

@router.post("/predict/bordeaux", summary="Estime le prix au m² à Bordeaux")
async def predict_bordeaux(request: PredictionRequest):
    return model_services.get_predict_bordeaux(request)

@router.post("/predict", summary="Estime le prix au m² de manière dynamique selon la ville")
async def predict_dynamique(request: DynamicPredictionRequest):
    ville = request.ville.lower()
    features = request.features

    if ville == "lille":
        return model_services.get_predict_lille(features)
    elif ville == "bordeaux":
        return model_services.get_predict_bordeaux(features)
    else:
        raise HTTPException(status_code=400, detail=f"Ville non reconnue : {request.ville}")
