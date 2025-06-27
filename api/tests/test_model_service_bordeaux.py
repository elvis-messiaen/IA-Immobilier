from services.model_services import ModelService
from schemas import PredictionRequest

class TestModelServiceBordeaux:
    def setup_method(self):
        self.service = ModelService()

    def test_linearregression_appartements_bordeaux(self):
        req = PredictionRequest(
            surface_bati=95,
            nombre_pieces=3,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=0,
            model="LinearRegression",
            type_bien="appartements"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "LinearRegression"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_linearregression_maisons_bordeaux(self):
        req = PredictionRequest(
            surface_bati=130,
            nombre_pieces=5,
            type_local="Maison",
            surface_terrain=320,
            nombre_lots=2,
            model="LinearRegression",
            type_bien="maisons"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "LinearRegression"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_decisiontree_appartements_bordeaux(self):
        req = PredictionRequest(
            surface_bati=80,
            nombre_pieces=2,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=1,
            model="DecisionTreeRegressor",
            type_bien="appartements"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "DecisionTreeRegressor"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_decisiontree_maisons_bordeaux(self):
        req = PredictionRequest(
            surface_bati=145,
            nombre_pieces=6,
            type_local="Maison",
            surface_terrain=500,
            nombre_lots=2,
            model="DecisionTreeRegressor",
            type_bien="maisons"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "DecisionTreeRegressor"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_randomforest_appartements_bordeaux(self):
        req = PredictionRequest(
            surface_bati=102,
            nombre_pieces=3,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=0,
            model="RandomForestRegressor",
            type_bien="appartements"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "RandomForestRegressor"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_randomforest_maisons_bordeaux(self):
        req = PredictionRequest(
            surface_bati=155,
            nombre_pieces=6,
            type_local="Maison",
            surface_terrain=580,
            nombre_lots=1,
            model="RandomForestRegressor",
            type_bien="maisons"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "RandomForestRegressor"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_xgboost_appartements_bordeaux(self):
        req = PredictionRequest(
            surface_bati=90,
            nombre_pieces=3,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=1,
            model="XGBoost",
            type_bien="appartements"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "XGBoost"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)

    def test_xgboost_maisons_bordeaux(self):
        req = PredictionRequest(
            surface_bati=170,
            nombre_pieces=7,
            type_local="Maison",
            surface_terrain=620,
            nombre_lots=3,
            model="XGBoost",
            type_bien="maisons"
        )
        resp = self.service.get_predict_bordeaux(req)
        assert resp.model == "XGBoost"
        assert resp.ville_modele == "Bordeaux"
        assert isinstance(resp.prix_m2_estime, float)
