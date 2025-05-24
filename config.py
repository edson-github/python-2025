from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# print(os.environ)
# Access environment variables
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'python_course')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

