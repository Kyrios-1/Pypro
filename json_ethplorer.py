import urllib.parse
import requests

main_api = 'https://api.ethplorer.io/getAddressInfo/0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98?'
api_key = 'freekey'
url = main_api + urllib.parse.urlencode({'apiKey':api_key})
json_data = requests.get(url).json()
token_Details = json_data['tokens']

for item in token_Details:
    token_Details = item['tokenInfo']
    if token_Details['name'] == str('SingularDTV'):
        print(str(token_Details['name'])+" "+"Hodlers"+": "+str(token_Details['holdersCount']))
