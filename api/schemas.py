from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    surface_bati: float = Field(..., gt=0)
    nombre_pieces: int = Field(..., ge=1)
    type_local: str
    surface_terrain: float = Field(..., ge=0)
    nombre_lots: int = Field(..., ge=0)
    model: str = Field(..., description="Nom du modèle à utiliser")
    type_bien: str = Field(..., description="appartements ou maisons")

class PredictionResponse(BaseModel):
    prix_m2_estime: float
    ville_modele: str
    model: str

class DynamicPredictionRequest(BaseModel):
    ville: str
    features: PredictionRequest
