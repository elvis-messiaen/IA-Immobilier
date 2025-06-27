from services.model_services import ModelService
from schemas import PredictionRequest


class TestModelServiceLille:
    def setup_method(self):
        self.service = ModelService()

    def test_linearregression_appartements_lille(self):
        req = PredictionRequest(
            surface_bati=100,
            nombre_pieces=4,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=1,
            model="LinearRegression",
            type_bien="appartements"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "LinearRegression"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_linearregression_maisons_lille(self):
        req = PredictionRequest(
            surface_bati=120,
            nombre_pieces=5,
            type_local="Maison",
            surface_terrain=300,
            nombre_lots=2,
            model="LinearRegression",
            type_bien="maisons"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "LinearRegression"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_decisiontree_appartements_lille(self):
        req = PredictionRequest(
            surface_bati=85,
            nombre_pieces=3,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=0,
            model="DecisionTreeRegressor",
            type_bien="appartements"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "DecisionTreeRegressor"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_decisiontree_maisons_lille(self):
        req = PredictionRequest(
            surface_bati=140,
            nombre_pieces=6,
            type_local="Maison",
            surface_terrain=450,
            nombre_lots=1,
            model="DecisionTreeRegressor",
            type_bien="maisons"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "DecisionTreeRegressor"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_randomforest_appartements_lille(self):
        req = PredictionRequest(
            surface_bati=95,
            nombre_pieces=4,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=2,
            model="RandomForestRegressor",
            type_bien="appartements"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "RandomForestRegressor"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_randomforest_maisons_lille(self):
        req = PredictionRequest(
            surface_bati=160,
            nombre_pieces=7,
            type_local="Maison",
            surface_terrain=600,
            nombre_lots=1,
            model="RandomForestRegressor",
            type_bien="maisons"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "RandomForestRegressor"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_xgboost_appartements_lille(self):
        req = PredictionRequest(
            surface_bati=88,
            nombre_pieces=3,
            type_local="Appartement",
            surface_terrain=0,
            nombre_lots=1,
            model="XGBoost",
            type_bien="appartements"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "XGBoost"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)

    def test_xgboost_maisons_lille(self):
        req = PredictionRequest(
            surface_bati=150,
            nombre_pieces=5,
            type_local="Maison",
            surface_terrain=350,
            nombre_lots=2,
            model="XGBoost",
            type_bien="maisons"
        )
        resp = self.service.get_predict_lille(req)
        assert resp.model == "XGBoost"
        assert resp.ville_modele == "Lille"
        assert isinstance(resp.prix_m2_estime, float)
