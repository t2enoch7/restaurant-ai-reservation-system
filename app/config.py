from dotenv import load_dotenv
import os

load_dotenv()  # Automatically reads from .env

# Example usage:
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")
APP_PORT = int(os.getenv("APP_PORT", 8000))

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://localhost:8000")
RESERVATION_TABLE = os.getenv("RESERVATION_TABLE", "Reservations")
