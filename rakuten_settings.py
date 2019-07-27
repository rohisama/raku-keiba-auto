import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RAKUTEN_ID = os.environ.get("RAKUTEN_ID")
RAKUTEN_PW = os.environ.get("RAKUTEN_PW")
RAKUTEN_PIN = os.environ.get("RAKUTEN_PIN")