
#!/usr/bin/env python2.7  
# coding=<UTF-8>
# tweetpic.py take a photo with the Pi camera and tweet it  
# by Alex Eames http://raspi.tv/?p=5918  
import tweepy
from subprocess import call
from datetime import datetime

import requests
import json

i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
cmd = 'raspistill -t 500 -w 1024 -h 768 -o  /home/pi/Pictures' + photo_name
call ([cmd], shell=True)         #shoot the photo  

def pick_values(sensor):
    # Sensordaten fr SDS011 und DHT11 abfragen
    # dazu die api von luftdaten.info nutzen
    # Peter Furle @Alpensichtung Hotzenwald 04 2017
    r = requests.get(sensor)
    json_string = r.text
    parsed_json = json.loads(json_string)
    # pretty print um uberhaupt zu verstehen was da passiert
    # print json.dumps(parsed_json, sort_keys=True, indent=4, separators=(',','$
    l = len(parsed_json)-1
    a = len(parsed_json[l]['sensordatavalues'])
    if a == 1:
        result=(parsed_json[l]['sensordatavalues'][0]['value_type'])+": "+(pars$
    if a == 2:
        result=(parsed_json[l]['sensordatavalues'][0]['value_type'])+": "+(pars$
        result=result+" "+(parsed_json[l]['sensordatavalues'][1]['value_type'])$
    return(result)



# Freiburger Sensor von sbamueller
url = 'http://api.luftdaten.info/static/v1/sensor/534/'
tweet = pick_values(url)

url = 'http://api.luftdaten.info/static/v1/sensor/533/'
tweet = tweet + " " + pick_values(url)
# Texte 140 Zeichen Tweets
tweet = tweet.replace('temperature: ','| Temp C:')
tweet = tweet.replace('P1:','|  PM10:')
tweet = tweet.replace('P2:','PM2.5:')

#print(tweet)


# Consumer keys and access tokens, used for OAuth  
CONSUMER_KEY = 'ihrKey'
CONSUMER_SECRET = 'ihrKey'
ACCESS_KEY = 'ihrKey'
ACCESS_SECRET = 'ihrKey'

# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY , ACCESS_SECRET)

# Creation of the actual interface, using authentication  
api = tweepy.API(auth)

# Send the tweet with photo  
photo_path = '/home/pi/Pictures' + photo_name
status = 'Blick auf Freiburg mit Feinstaubwerten, Temp & Luftfeuchte ' + i.strf$
status = status + tweet
api.update_with_media(photo_path, status=status)


