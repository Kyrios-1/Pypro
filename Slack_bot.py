'''slackbot to post data from ethplorer'''

import urllib.parse
import requests
from slacker import Slacker

def check_wallets(token_contract, api_key, slack_token, slack_channel):
    '''Check wallet function(this is 2 functions in one, need to spilt  ethplorer/slack)'''

    #encode url & request data from ethplorer
    url = ('https://api.ethplorer.io/getTokenInfo/'
           + token_contract +'?'+ urllib.parse.urlencode({'apiKey':api_key}))

    json_data = requests.get(url).json()

    #format message
    message = ("Hi, Today we have" + " " + str(json_data['holdersCount']) + " "
               + "wallets containing" + " " + str(json_data['symbol']))

    #Post message to slack
    slack = Slacker(slack_token)
    slack.chat.post_message(channel=slack_channel, text=message, as_user=True)

check_wallets('0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009', 'freekey', 'xoxb-189051142021-A6zoOt0Hk6QLdZK5GVCWyMLX', '#general')

#todo: error handling, run once a day
