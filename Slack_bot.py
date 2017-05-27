"""Slackbot to post data from ethplorer"""
import urllib.parse
import requests
from slacker import Slacker

#ethplorer constants
MAIN_API = 'https://api.ethplorer.io/getTokenInfo/0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009?'
API_KEY = 'freekey'
#slack constants
TOKEN = 'xoxb-189756199703-7LsrYwVXdfULLdqYtUyG75Zf'
SLACK = Slacker(TOKEN)

#grab data from ethplorer
URL = MAIN_API + urllib.parse.urlencode({'apiKey':API_KEY})
JSON_DATA = requests.get(URL).json()

#post on slack
#SLACK.chat.post_message('#general', str(JSON_DATA['symbol'])+" "+"Hodlers"+": "+str(JSON_DATA['holdersCount']))
SLACK.chat.post_message('#general', "Today we have" + " " + str(JSON_DATA['holdersCount']) + " " + "wallets containing" + " " + str(JSON_DATA['symbol']))
