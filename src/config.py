import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_TOKEN_URL = os.getenv("API_TOKEN_URL")
REALM = os.getenv("REALM")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SCOPES = os.getenv("SCOPES")
CONTENT_TYPE = os.getenv("CONTENT_TYPE", "application/x-www-form-urlencoded")

# API Endpoints
JOB_OFFERS_URL = os.getenv("JOB_OFFERS_URL")

# Filters
DEPARTMENT = os.getenv("DEPARTMENT", "07")
CONTRACT_TYPE = os.getenv("CONTRACT_TYPE", "CDI")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Request Configuration
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))  # Default to 10 seconds if not provided

# Data paths
BRONZE_PATH = os.getenv("BRONZE_PATH", os.path.join("data", "bronze"))
SILVER_PATH = os.getenv("SILVER_PATH", os.path.join("data", "silver"))
GOLD_PATH = os.getenv("GOLD_PATH", os.path.join("data", "gold"))


# config.py

# Column renaming mappings for the offers table
COLUMN_RENAME_OFFERS = {
    "id": "offre_id",
    "intitule": "intitule",
    "description": "description",
    "dateCreation": "date_creation",
    "dateActualisation": "date_actualisation",
    "lieuTravail_libelle": "lieu_travail_libelle",
    "lieuTravail_latitude": "lieu_travail_latitude",
    "lieuTravail_longitude": "lieu_travail_longitude",
    "lieuTravail_codePostal": "lieu_travail_code_postal",
    "lieuTravail_commune": "lieu_travail_commune",
    "romeCode": "rome_code",
    "romeLibelle": "rome_libelle",
    "appellationlibelle": "appellation_libelle",
    "typeContrat": "type_contrat",
    "typeContratLibelle": "type_contrat_libelle",
    "natureContrat": "nature_contrat",
    "experienceExige": "experience_exige",
    "experienceLibelle": "experience_libelle",
    "experienceCommentaire": "experience_commentaire",
    "salaire_libelle": "salaire_libelle",
    "salaire_commentaire": "salaire_commentaire",
    "salaire_complement1": "salaire_complement_1",
    "salaire_complement2": "salaire_complement_2",
    "dureeTravailLibelle": "duree_travail_libelle",
    "dureeTravailLibelleConverti": "duree_travail_libelle_converti",
    "complementExercice": "complement_exercice",
    "conditionExercice": "condition_exercice",
    "alternance": "alternance",
    "contact_nom": "contact_nom",
    "contact_coordonnees1": "contact_coordonnees_1",
    "contact_coordonnees2": "contact_coordonnees_2",
    "contact_coordonnees3": "contact_coordonnees_3",
    "contact_courriel": "contact_courriel",
    "contact_urlPostulation": "contact_url_postulation",
    "contact_telephone": "contact_telephone",
    "agence_courriel": "agence_courriel",
    "nombrePostes": "nombre_postes",
    "accessibleTH": "accessible_th",
    "deplacementCode": "deplacement_code",
    "deplacementLibelle": "deplacement_libelle",
    "qualificationCode": "qualification_code",
    "qualificationLibelle": "qualification_libelle",
    "codeNAF": "code_naf",
    "secteurActivite": "secteur_activite",
    "secteurActiviteLibelle": "secteur_activite_libelle",
    "origineOffre_origine": "origine_offre_origine",
    "origineOffre_urlOrigine": "origine_offre_url_origine",
    "offresManqueCandidats": "offres_manque_candidats",
    "contexteTravail_horaires": "contexte_travail_horaires",
    "contexteTravail_conditionsExercice": "contexte_travail_conditions_exercice",
    "qualitesProfessionnelles": "qualites_professionnelles",
    "formations": "formations",
    "langues": "langues",
    "permis": "permis",
}

STRING_COLUMNS_OFFERS = [
    "offre_id",
    "intitule",
    "description",
    "lieu_travail_libelle",
    "lieu_travail_code_postal",
    "lieu_travail_commune",
    "rome_code",
    "rome_libelle",
    "appellation_libelle",
    "type_contrat",
    "type_contrat_libelle",
    "nature_contrat",
    "experience_exige",
    "experience_libelle",
    "experience_commentaire",
    "salaire_libelle",
    "salaire_commentaire",
    "salaire_complement_1",
    "salaire_complement_2",
    "duree_travail_libelle",
    "duree_travail_libelle_converti",
    "complement_exercice",
    "condition_exercice",
    "contact_nom",
    "contact_coordonnees_1",
    "contact_coordonnees_2",
    "contact_coordonnees_3",
    "contact_courriel",
    "contact_url_postulation",
    "contact_telephone",
    "agence_courriel",
    "deplacement_code",
    "deplacement_libelle",
    "qualification_code",
    "qualification_libelle",
    "code_naf",
    "secteur_activite",
    "secteur_activite_libelle",
    "tranche_effectif_etab",
    "origine_offre_origine",
    "origine_offre_url_origine",
    "contexte_travail_horaires",
    "contexte_travail_conditions_exercice",
]

BOOLEAN_COLUMNS_OFFERS = [
    "alternance",
    "accessible_th",
    "offres_manque_candidats",
]

INTEGER_COLUMNS_OFFERS = [
    "nombre_postes",
]

DOUBLE_COLUMNS_OFFERS = [
    "lieu_travail_latitude",
    "lieu_travail_longitude",
]

DATE_COLUMNS_OFFERS = [
    "date_creation",
    "date_actualisation",
]

SELECT_COLUMNS_OFFERS = list(COLUMN_RENAME_OFFERS.values())

# Configurations for entreprises
COLUMN_RENAME_ENTREPRISES = {
    "entreprise_nom": "entreprise_nom",
    "entreprise_description": "entreprise_description",
    "entreprise_logo": "entreprise_logo",
    "entreprise_url": "entreprise_url",
    "entreprise_entrepriseAdaptee": "entreprise_entreprise_adaptee",
}

STRING_COLUMNS_ENTREPRISES = [
    "entreprise_nom",
    "entreprise_description",
    "entreprise_logo",
    "entreprise_url",
]

BOOLEAN_COLUMNS_ENTREPRISES = [
    "entreprise_entreprise_adaptee",
]

SELECT_COLUMNS_ENTREPRISES = list(COLUMN_RENAME_ENTREPRISES.values())

# Configurations for competences
COLUMN_RENAME_COMPETENCES = {
    "competences_code": "competences_code",
    "competences_libelle": "competences_libelle",
    "competences_exigence": "competences_exigence",
}

STRING_COLUMNS_COMPETENCES = [
    "competences_code",
    "competences_libelle",
    "competences_exigence",
]

SELECT_COLUMNS_COMPETENCES = list(COLUMN_RENAME_COMPETENCES.values())
