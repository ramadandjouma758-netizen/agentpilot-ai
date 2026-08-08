import os

from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
APP_NAME = os.getenv("APP_NAME", "AgentPilot AI")
DATABASE_URL = os.getenv("DATABASE_URL", "")
