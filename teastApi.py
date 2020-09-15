import requests
from wit import Wit
def getType(msg):
    if msg!="":
        access_token="IPBSNY34NCDVAB7H65I7N5K4EYXQAGRG"
        client = Wit(access_token)
        return (client.message(msg)['entities']['intent'][0]['value'])
