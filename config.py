import os

from dotenv import load_dotenv

load_dotenv()

# environment
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

# SETTINGS
UPLOADED_FILES_PATH = "uploaded_files/"
