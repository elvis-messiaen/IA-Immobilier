# IA-Immobilier

**API de prédiction du prix au m² pour Lille et Bordeaux, basée sur l'IA et le Machine Learning.**

---

## Sommaire

1. [Présentation](#présentation)
2. [Fonctionnalités](#fonctionnalités)
3. [Architecture et Structure du Projet](#architecture-et-structure-du-projet)
4. [Installation (Windows, macOS, Linux)](#installation)
5. [Configuration des variables d'environnement](#configuration-des-variables-denvironnement)
6. [Lancement du projet (API + Frontend)](#lancement-du-projet-api-frontend)
7. [Documentation de l'API](#documentation-de-lapi)
8. [Exemples de requêtes](#exemples-de-requêtes)
9. [Tests et Qualité](#tests-et-qualité)
10. [Dépendances](#dépendances)
11. [Modèles IA utilisés](#modèles-ia-utilisés)
12. [Bonnes pratiques et sécurité](#bonnes-pratiques-et-sécurité)
13. [FAQ](#faq)
14. [Contribuer](#contribuer)
15. [Licence](#licence)
16. [Contact](#contact)

---

## Présentation

**IA-Immobilier** est une API RESTful développée en Python avec FastAPI, permettant d'estimer le prix au m² de biens immobiliers à Lille et Bordeaux, pour appartements et maisons, à l'aide de modèles de Machine Learning (Linear Regression, Decision Tree, Random Forest, XGBoost).  
Le projet inclut :
- Un backend API robuste et documenté
- Un frontend simple pour la saisie des données et l'affichage des résultats
- Des notebooks de modélisation et d'entraînement
- Des tests unitaires pour garantir la fiabilité

---

## Fonctionnalités

- Prédiction du prix au m² pour Lille et Bordeaux
- Choix du modèle de Machine Learning utilisé
- Support des types de biens : appartements et maisons
- Frontend web pour la saisie et la visualisation
- API RESTful documentée (OpenAPI/Swagger)
- Tests unitaires automatisés
- Facilement extensible à d'autres villes ou modèles

---

## Architecture et Structure du Projet

```
IA&Immobilier/
│
├── api/                  # Backend FastAPI
│   ├── app/frontend/     # Frontend HTML/CSS/JS
│   ├── main.py           # Point d'entrée FastAPI
│   ├── routes/           # Endpoints API
│   ├── schemas.py        # Schémas Pydantic
│   ├── services/         # Logique métier et chargement des modèles
│   ├── tests/            # Tests unitaires
│   └── package.json      # Dépendances JS (si besoin)
│
├── app/                  # Scripts et outils ML
│   ├── main.py
│   ├── model_loader.py
│   ├── predict.py
│   └── schemas.py
│
├── models/               # Notebooks d'entraînement des modèles
│   ├── model_bordeaux.ipynb
│   └── model_lille.ipynb
│
├── donnees/              # Scripts d'extraction de données
│
├── data/                 # Données et modèles sauvegardés
│
├── requirements.txt      # Dépendances Python
├── pytest.ini            # Config tests
├── launch_form.py        # Lancement du frontend
└── README.md             # Ce fichier
```

---

## Installation

### Prérequis

- Python 3.10+ (compatible Windows, macOS, Linux)
- pip (installé avec Python)
- (Optionnel) Node.js si vous souhaitez modifier le frontend

### 1. Cloner le dépôt

```bash
git clone https://github.com/elvis-messiaen/IA-Immobilier.git
cd IA-Immobilier
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances Python

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. (Optionnel) Installer les dépendances JS pour le frontend

```bash
cd api/app/frontend
npm install
```

---

## Configuration des variables d'environnement

Créez un fichier `.env` dans le dossier `api/` si besoin (ex : pour des clés API, chemins personnalisés, etc.).  
Exemple de variables :

```
# Exemple .env
MODEL_BASE_PATH=data/sauvegardes
```

---

## Lancement du projet (API + Frontend)

Pour démarrer l'ensemble de la solution (API + interface graphique) :

1. Ouvrez un **premier terminal** et lancez le backend FastAPI :

```bash
uvicorn api.main:app --reload
```

2. Ouvrez un **second terminal** et lancez l'interface graphique HTML :

```bash
python launch_form.py
```

Cela ouvrira automatiquement la fenêtre HTML (predict_lille_form.html) dans votre navigateur.

Remplissez le formulaire et cliquez sur « Estimer » pour obtenir une prédiction.

L'API sera accessible sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Documentation interactive (Swagger)

La documentation interactive Swagger est disponible sur [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Vous pouvez **consulter et tester tous les endpoints** directement via cette interface web, sans avoir besoin d'outil externe.

---

## Lancer les tests

Pour exécuter les tests unitaires et vérifier le bon fonctionnement de l'API et des modèles :

1. Assurez-vous que les dépendances sont installées et que l'environnement virtuel est activé.
2. Depuis la racine du projet, lancez simplement :

```bash
pytest
```

Les tests couvrent la logique de prédiction pour chaque ville, type de bien et modèle. Les résultats s'afficheront dans le terminal.

---

## Documentation de l'API

### Endpoints principaux

- `POST /models/predict/lille`  
  Prédiction pour Lille

- `POST /models/predict/bordeaux`  
  Prédiction pour Bordeaux

- `POST /models/predict`  
  Prédiction dynamique selon la ville

#### Exemple de payload JSON

```json
{
  "surface_bati": 100,
  "nombre_pieces": 4,
  "type_local": "Appartement",
  "surface_terrain": 0,
  "nombre_lots": 1,
  "model": "LinearRegression",
  "type_bien": "appartements"
}
```

#### Exemple de réponse

```json
{
  "prix_m2_estime": 3200.50,
  "ville_modele": "Lille",
  "model": "LinearRegression"
}
```

---

## Exemples de requêtes

### Avec `curl`

```bash
curl -X POST "http://127.0.0.1:8000/models/predict/lille" \
     -H "Content-Type: application/json" \
     -d '{"surface_bati": 100, "nombre_pieces": 4, "type_local": "Appartement", "surface_terrain": 0, "nombre_lots": 1, "model": "LinearRegression", "type_bien": "appartements"}'
```

---

## Tests et Qualité

Lancez les tests unitaires avec :

```bash
pytest
```

Les tests couvrent la logique de prédiction pour chaque ville, type de bien et modèle.

---

## Dépendances

Principales :

- Python : pandas, numpy, scikit-learn, joblib, requests, fastapi, uvicorn, pydantic, xgboost, pytest
- JS (frontend) : (optionnel, voir package.json)

Voir `requirements.txt` pour la liste complète.

---

## Modèles IA utilisés

- **LinearRegression**
- **DecisionTreeRegressor**
- **RandomForestRegressor**
- **XGBoost**

Les modèles sont entraînés via les notebooks dans `models/` et sauvegardés dans `data/sauvegardes/`.

---

## Bonnes pratiques et sécurité

- Ne jamais exposer de données sensibles dans le code ou le .env
- Toujours utiliser un environnement virtuel
- Garder les dépendances à jour
- Ajouter des tests pour toute nouvelle fonctionnalité

---

## FAQ

**Q : Peut-on ajouter d'autres villes ou modèles ?**  
R : Oui, il suffit d'entraîner un modèle et de l'ajouter dans `data/sauvegardes/` puis de l'intégrer dans le code.

**Q : L'API est-elle déployable sur le cloud ?**  
R : Oui, compatible avec tout service supportant FastAPI (Heroku, Azure, AWS, etc.)

---

## Contribuer

Les contributions sont les bienvenues !  
Merci de créer une issue ou une pull request.

---

## Licence

Ce projet est sous licence MIT.

---

## Contact

Pour toute question :  
[elvis-messiaen@protonmail.com](mailto:elvis-messiaen@protonmail.com)
