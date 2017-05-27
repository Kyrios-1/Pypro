"""Download json with Bittrex wallet details from ethplorer extract token name & holder count"""

import urllib.parse
import requests

MAIN_API = 'https://api.ethplorer.io/getTokenInfo/0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009?'
API_KEY = 'freekey'
URL = MAIN_API + urllib.parse.urlencode({'apiKey':API_KEY})
JSON_DATA = requests.get(URL).json()
#TOKEN_DETAILS = JSON_DATA['tokens']

for item in JSON_DATA:
    TOKEN_DETAILS = item['tokenInfo']
    if TOKEN_DETAILS['name'] == str('SingularDTV'):
        print(str(TOKEN_DETAILS['name'])+" "+"Hodlers"+": "+str(TOKEN_DETAILS['holdersCount']))
