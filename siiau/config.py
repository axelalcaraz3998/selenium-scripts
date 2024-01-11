import os
from dotenv import load_dotenv

# Supported browsers: chrome, firefox, edge, headlesschrome, headlessfirefox, headlessedge
BROWSER = 'chrome'

# Credentials
load_dotenv()
CODE = os.getenv('CODIGO')
NIP = os.getenv('NIP')