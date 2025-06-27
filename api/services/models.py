import os
import joblib

class ModelLoader:
    def __init__(self, base_path="data/sauvegardes"):
        self.base_path = base_path
        self.model_map = {
            "LinearRegression": "LinearRegression",
            "DecisionTreeRegressor": "DecisionTreeRegressor",
            "RandomForestRegressor": "RandomForestRegressor",
            "XGBoost": "XGBRegressor"
        }

    def load(self, model_name: str, type_bien: str):
        model_name = model_name.strip()
        type_bien = type_bien.strip().lower()

        if model_name not in self.model_map:
            raise ValueError(f"Modèle non reconnu : {model_name}")

        mapped_name = self.model_map[model_name]

        dossier = os.path.join(self.base_path, mapped_name, type_bien)
        if not os.path.exists(dossier):
            raise FileNotFoundError(f"Dossier introuvable : {dossier}")

        nom_modele = f"app_model_{model_name}.pkl"
        path_model = os.path.join(dossier, nom_modele)
        path_scaler_X = os.path.join(dossier, "app_scaler_X.pkl")
        path_scaler_y = os.path.join(dossier, "app_scaler_y.pkl")

        if not os.path.isfile(path_model):
            raise FileNotFoundError(f"Modèle non trouvé : {path_model}")
        if not os.path.isfile(path_scaler_X) or not os.path.isfile(path_scaler_y):
            raise FileNotFoundError("Scaler(s) manquant(s)")

        model = joblib.load(path_model)
        scaler_X = joblib.load(path_scaler_X)
        scaler_y = joblib.load(path_scaler_y)

        return {
            "model": model,
            "scaler_X": scaler_X,
            "scaler_y": scaler_y,
            "nom": model_name,
            "type_bien": type_bien
        }