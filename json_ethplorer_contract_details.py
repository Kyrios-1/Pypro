import urllib.parse
import requests

MAIN_API = 'https://api.ethplorer.io/getTokenInfo/0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009?'
API_KEY = 'freekey'
URL = MAIN_API + urllib.parse.urlencode({'apiKey':API_KEY})
JSON_DATA = requests.get(URL).json()

print(str(JSON_DATA['symbol'])+" "+"Hodlers"+": "+str(JSON_DATA['holdersCount']))
