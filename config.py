import os
import dotenv

dotenv.load_dotenv('.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')

DJANGO_SECRET = os.getenv('DJANGO_SECRET')

DB_NAME = os.getenv('DB_NAME')
DB_LOGIN = os.getenv('DB_LOGIN')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
