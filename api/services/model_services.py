from api.schemas import PredictionRequest, PredictionResponse
from api.services.models import ModelLoader
import numpy as np

class ModelService:
    def __init__(self):
        self.loader = ModelLoader()
        self.type_local_map = {
            "Maison": 0,
            "Appartement": 1
        }

    def get_predict_lille(self, data: PredictionRequest) -> PredictionResponse:
        return self._predict(data, ville="Lille")

    def get_predict_bordeaux(self, data: PredictionRequest) -> PredictionResponse:
        return self._predict(data, ville="Bordeaux")

    def _predict(self, data: PredictionRequest, ville: str) -> PredictionResponse:
        model_obj = self.loader.load(data.model, data.type_bien)

        if data.type_local not in self.type_local_map:
            raise ValueError(f"type_local inconnu : {data.type_local}")

        type_local = self.type_local_map[data.type_local]

        X = np.array([[
            data.surface_bati,
            data.nombre_pieces,
            data.surface_terrain,
            data.nombre_lots,
            type_local
        ]])

        X_scaled = model_obj["scaler_X"].transform(X)
        y_scaled = model_obj["model"].predict(X_scaled)
        y_pred = model_obj["scaler_y"].inverse_transform(y_scaled.reshape(-1, 1))

        return PredictionResponse(
            prix_m2_estime=round(float(y_pred[0][0]), 2),
            ville_modele=ville,
            model=data.model
        )
