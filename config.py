import os
import dotenv

dotenv.load_dotenv('.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')
DJANGO_SECRET = os.getenv('DJANGO_SECRET')
