# France Travail Offres - Pipeline de Traitement de Données

## Description

Ce projet implémente un pipeline complet pour extraire, transformer et charger (ETL) des données d'offres d'emploi depuis une API externe. Le pipeline est conçu pour automatiser toutes les étapes du traitement des données, en commençant par l'extraction des données brutes jusqu'à la production des données transformées et prêtes à être consommées.

---

## Structure du Projet

├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
├── logs/
│   └── app.log
├── src/
│   ├── pipelines/
│   │   ├── bronze_layer.py
│   │   ├── silver_layer.py
│   │   ├── gold_layer.py
│   ├── api_client.py
│   ├── token_manager.py
│   ├── config.py
│   ├── logging_setup.py
│   ├── utils.py
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── test_api_client.py
│   ├── test_token_manager.py
│   ├── test_utils.py
│   ├── test_bronze_layer.py
│   ├── test_silver_layer.py
│   ├── test_gold_layer.py
│   ├── test_integration_pipeline.py
├── venv/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt


---

## Prérequis

1. **Python 3.8+** : Assurez-vous que Python est installé sur votre machine.
2. **Virtualenv** : Utilisez un environnement virtuel pour gérer les dépendances.
3. **Variables d'environnement** :
   Créez un fichier `.env` à la racine avec les clés suivantes :
   ```dotenv
   API_TOKEN_URL=
   REALM=
   CLIENT_ID=
   CLIENT_SECRET=
   SCOPES=
   JOB_OFFERS_URL=
   BRONZE_PATH=data/bronze
   SILVER_PATH=data/silver
   GOLD_PATH=data/gold
   LOG_LEVEL=INFO
   REQUEST_TIMEOUT=10

## Installation

Clonez le dépôt:
**git clone <url-du-depot>**
**cd france-travail-offres**

### Installez les dépendances :

**python -m venv venv**
**source venv/bin/activate**  # Sur Windows : venv\Scripts\activate
**pip install -r requirements.txt**

### Configurez les variables d'environnement :

**cp .env.example .env**

### Créez les dossiers nécessaires :

**mkdir -p data/bronze data/silver data/gold**

## Utilisation

### Exécution du Pipeline Complet:
Pour exécuter tout le pipeline ETL :

**python src/main.py**

Le pipeline exécutera successivement les étapes suivantes :

Récupération du jeton d'authentification.
- Extraction des données depuis l'API et sauvegarde dans le dossier bronze.
- Transformation des données brutes en tables structurées dans le dossier silver.
- Application des transformations finales et export des données finales dans le dossier gold.


## Journaux

Tous les journaux d'exécution sont stockés dans le fichier logs/app.log. Les niveaux de journalisation peuvent être configurés dans le fichier **.env** via la variable **LOG_LEVEL.**

## Tests

Pour exécuter les tests unitaires :

**pytest**

Les tests couvrent les modules suivants :

Gestion des jetons (token_manager.py)
Appels API (api_client.py)
Transformation des données (bronze_layer.py, silver_layer.py, gold_layer.py)
Utilitaires (utils.py)
