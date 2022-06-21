import os

from dotenv import load_dotenv
from functions.sleep import *
from functions.load_keys import load_env_variables

VERSION = 1.0
load_dotenv()

print("Twitter Video Maker Bot")
print("version", VERSION)

sleep_3()

load_env_variables()







