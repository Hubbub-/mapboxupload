from urllib2 import urlopen
import json
import geojson
from pprint import pprint
import os

#

time = []
lat = []
lon = []
point = []
feature = []

data_file = urlopen("https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/0N6dXjTo7eRCUfsNlXrLNnfDFuDVNVN1c/message.json") 
# data_file = urlopen('https://raw.githubusercontent.com/Hubbub-/mapboxupload/master/rawmessage.json')
data = json.load(data_file)


count = 0
dataAvailable = True

while dataAvailable:
  try:
    time.append (data["response"]["feedMessageResponse"]["messages"]["message"][count]["dateTime"])
    lat.append (data["response"]["feedMessageResponse"]["messages"]["message"][count]["latitude"])
    lon.append (data["response"]["feedMessageResponse"]["messages"]["message"][count]["longitude"])
    count += 1
    pprint(count)
  except Exception:
    pprint("end of data")
    dataAvailable = False
    pass



# time = data["response"]["feedMessageResponse"]["messages"]["message"][0]["dateTime"]

# lat = data["response"]["feedMessageResponse"]["messages"]["message"][0]["latitude"]
# longitude = data["response"]["feedMessageResponse"]["messages"]["message"][0]["longitude"]

#coordinates = str(longitude) + ", " + str(lat)

for index in range(len(time)):
  point.append(geojson.Point((lon[index], lat[index])))

  feature.append(geojson.Feature(geometry=point[index], properties={"title": "Vlog 1", "marker-color": "#f86767", "marker-size": "large", "marker-symbol": "star", "url": "https://www.youtube.com/watch?v=ty5Cl9GbbGs", "time": time[index]}))


# point1 = geojson.Point((lon, lat))

# myFeature1 = geojson.Feature(geometry=point1, properties={"title": "Vlog 1", "marker-color": "#f86767", "marker-size": "large", "marker-symbol": "star", "url": "https://www.youtube.com/watch?v=ty5Cl9GbbGs"})

collection = geojson.FeatureCollection(feature)


with open("datatest.geojson", 'w') as outfile:
  geojson.dump(collection, outfile, sort_keys=True,indent=4, separators=(',', ': '))

pprint(collection)