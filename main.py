import os

from dotenv import load_dotenv
from sleep import *

VERSION = 1.0
load_dotenv()

print("Twitter Video Maker Bot")
print("version", VERSION)

sleep_3()



TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

