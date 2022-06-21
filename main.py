import time
import os

VERSION = 1.0

from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

