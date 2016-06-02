import urllib2
import json
from pprint import pprint
import os

#newdata = urllib2.urlopen("https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/0N6dXjTo7eRCUfsNlXrLNnfDFuDVNVN1c/message.json")



with open('rawmessage.json') as data_file:    
    data = json.load(data_file)

selectdata = data["response"]["feedMessageResponse"]["messages"]["message"][1]["dateTime"]
pprint(selectdata)