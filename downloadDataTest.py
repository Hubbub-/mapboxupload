import urllib2
import json
import geojson
from pprint import pprint
import os

#newdata = urllib2.urlopen("https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/0N6dXjTo7eRCUfsNlXrLNnfDFuDVNVN1c/message.json")



with open('rawmessage.json') as data_file:    
    data = json.load(data_file)

time = data["response"]["feedMessageResponse"]["messages"]["message"][0]["dateTime"]

lat = data["response"]["feedMessageResponse"]["messages"]["message"][0]["latitude"]
longitude = data["response"]["feedMessageResponse"]["messages"]["message"][0]["longitude"]

coordinates = str(longitude) + ", " + str(lat)

point1 = geojson.Point((longitude, lat))

myFeature1 = geojson.Feature(geometry=point1, properties={"title": "Vlog 1", "marker-color": "#f86767", "marker-size": "large", "marker-symbol": "star", "url": "https://www.youtube.com/watch?v=ty5Cl9GbbGs"})


pprint(myFeature1)