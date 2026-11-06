# Titanic Survival Prediction - Deploiement Docker

Ce projet contient une application de prediction de survie pour le Titanic en utilisant un modele K-Nearest Neighbors (KNN). L'architecture est conteneurisee avec Docker et Docker Compose.

## Architecture du Projet
* api.py : API backend developpee avec FastAPI qui charge le modele et expose le point de terminaison /predict.
* app.py : Interface utilisateur frontend construite avec Streamlit pour saisir les donnees et interroger l'API.
* Dockerfile : Image pour encapsuler l'environnement Python et les dependances.
* docker-compose.yml : Orchestration des deux services (API sur le port 8000 et Streamlit sur le port 8501).

## Comment lancer l'application avec Docker

Executez cette commande dans le terminal a la racine du projet :

```bash
    docker-compose up --build
```

Emplacements :
* Interface graphique Streamlit : http://localhost:8501
* API FastAPI : http://localhost:8000/docs
