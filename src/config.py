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
