from services.models import ModelLoader
import pytest

def test_chargement_linearregression_appartements():
    loader = ModelLoader()
    model_obj = loader.load("LinearRegression", "appartements")
    assert model_obj["nom"] == "LinearRegression"
    assert model_obj["type_bien"] == "appartements"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_linearregression_maisons():
    loader = ModelLoader()
    model_obj = loader.load("LinearRegression", "maisons")
    assert model_obj["nom"] == "LinearRegression"
    assert model_obj["type_bien"] == "maisons"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_decisiontree_appartements():
    loader = ModelLoader()
    model_obj = loader.load("DecisionTreeRegressor", "appartements")
    assert model_obj["nom"] == "DecisionTreeRegressor"
    assert model_obj["type_bien"] == "appartements"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_decisiontree_maisons():
    loader = ModelLoader()
    model_obj = loader.load("DecisionTreeRegressor", "maisons")
    assert model_obj["nom"] == "DecisionTreeRegressor"
    assert model_obj["type_bien"] == "maisons"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_randomforest_appartements():
    loader = ModelLoader()
    model_obj = loader.load("RandomForestRegressor", "appartements")
    assert model_obj["nom"] == "RandomForestRegressor"
    assert model_obj["type_bien"] == "appartements"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_randomforest_maisons():
    loader = ModelLoader()
    model_obj = loader.load("RandomForestRegressor", "maisons")
    assert model_obj["nom"] == "RandomForestRegressor"
    assert model_obj["type_bien"] == "maisons"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_xgboost_appartements():
    loader = ModelLoader()
    model_obj = loader.load("XGBoost", "appartements")
    assert model_obj["nom"] == "XGBoost"
    assert model_obj["type_bien"] == "appartements"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]

def test_chargement_xgboost_maisons():
    loader = ModelLoader()
    model_obj = loader.load("XGBoost", "maisons")
    assert model_obj["nom"] == "XGBoost"
    assert model_obj["type_bien"] == "maisons"
    assert model_obj["model"]
    assert model_obj["scaler_X"]
    assert model_obj["scaler_y"]
