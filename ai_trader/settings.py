# settings for Django with MongoDBimport os
from pathlib import Path
from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "super-secret-key")
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Applications
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'ai_trader.urls'

TEMPLATES = []
WSGI_APPLICATION = 'ai_trader.wsgi.application'

# Static files for Render
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MongoDB Connection
connect(
    db=os.getenv("MONGO_DB", "ai_trader_db"),
    host=os.getenv("MONGO_URI", "mongodb://localhost:27017/ai_trader_db"),
    alias='default'
)

# Django REST Framework + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True
