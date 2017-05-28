"""slackbot to post data from ethplorer"""

import urllib.parse
import requests
from slacker import Slacker

#constants
API_DOM = 'api.ethplorer.io'
API_KEY = 'freekey'
API_METHOD = 'getTokenInfo'
TOKEN_CONTRACT = '0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009'
SLACK_TOKEN = 'xoxb-189051142021-A6zoOt0Hk6QLdZK5GVCWyMLX' #slack.com maps token to team
SLACK_CHANNEL = '#general'


URL = 'https://'+ API_DOM +'/'+ API_METHOD +'/'+ TOKEN_CONTRACT +'?'+ urllib.parse.urlencode({'apiKey':API_KEY}) #encode url
JSON_DATA = requests.get(URL).json() #grab data from ethplorer

MESSAGE = "Hi, Today we have" + " " + str(JSON_DATA['holdersCount']) + " " + "wallets containing" + " " + str(JSON_DATA['symbol']) #format message

SLACK = Slacker(SLACK_TOKEN) #pass token info to slacker
SLACK.chat.post_message(channel=SLACK_CHANNEL, text=MESSAGE, as_user=True) #post message on slack

#todo: error handling, run once a day
#def check_wallets(API_URL, API_KEY, API_METHOD, TOKEN_CONTRACT):
