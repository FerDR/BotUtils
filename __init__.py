from pathlib import Path
from Font import *
from Facebook import *

def getAccessToken(filename='access_token.txt'):
    return Path(filename).read_text().strip()

