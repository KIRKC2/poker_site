import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_URL = os.getenv("DB_URL")

DB_SERVER = os.getenv("DB_SERVER")