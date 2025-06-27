from fastapi import FastAPI
from api.routes import routes

app = FastAPI(
    title="API Estimation Immobilier",
    version="1.0.0",
    description="API de prédiction du prix au m² pour Lille et Bordeaux"
)

app.include_router(routes.router)
