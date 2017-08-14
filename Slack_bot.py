'''slackbot to post data from ethplorer'''

import urllib.parse
import requests
import socket
from slacker import Slacker

def ethplorer_request(token_contract, api_key):
    """
    Request json file from ethplorer via api, extract and return token symbol & wallet count.

    parameters:
                token_contract: A token contract address
                api_key: Ethplorer api key
    """
    #encode url & request json from ethplorer
    url = (
        'https://api.ethplorer.io/getTokenInfo/' + token_contract
        + '?' + urllib.parse.urlencode({'apiKey':api_key}))

    json_data = requests.get(url).json()
    #create a dictionary with chosen results
    return {'symbol' : str(json_data['symbol']), 'holdersCount' : str(json_data['holdersCount'])}

    #Except socket.error:

    #time.sleep(sleeptime)

def slack_post(slack_token, slack_channel):
    """
    assemble message text and post on slack

    parameters:
                slack_token: bot token from slack administrator
                slack_channel: channel to post message in
    """
    token_info = ethplorer_request('0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009', 'freekey')
    #construct message text
    message = (
        "Hi, Today we have" + " " + token_info['holdersCount'] + " "
        + "wallets containing" + " " + token_info['symbol'])

    #print(message)

    #Post message to slack
    slack = Slacker(slack_token)
    slack.chat.post_message(channel=slack_channel, text=message, as_user=True)

slack_post('xoxb-189051142021-A6zoOt0Hk6QLdZK5GVCWyMLX', '#general')
#todo: error handling, run once a day
