"""Download json with Bittrex wallet details from ethplorer extract token name & holder count"""

import urllib.parse
import requests

MAIN_API = 'https://api.ethplorer.io/getAddressInfo/0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98?'
API_KEY = 'freekey'
URL = MAIN_API + urllib.parse.urlencode({'apiKey':API_KEY})
JSON_DATA = requests.get(URL).json()
TOKEN_DETAILS = JSON_DATA['tokens']

for item in TOKEN_DETAILS:
    TOKEN_DETAILS = item['tokenInfo']
    if TOKEN_DETAILS['name'] == str('SingularDTV'):
        print(str(TOKEN_DETAILS['name'])+" "+"Hodlers"+": "+str(TOKEN_DETAILS['holdersCount']))
