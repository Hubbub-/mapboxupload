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
existingtimes = []
duplicates = []

print "\n\nStarting...\n"
#---- load the spot json feed ----

#spotjson = urlopen("https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/0N6dXjTo7eRCUfsNlXrLNnfDFuDVNVN1c/message.json") 
spotjson = urlopen('https://raw.githubusercontent.com/Hubbub-/mapboxupload/master/rawmessage.json')
spotdata = json.load(spotjson)

#---- load the existing geojson file ----
oldGeoFile = open('datatest.geojson')
oldData = geojson.load(oldGeoFile)

#---- make a list of existing features and times 
for times in oldData['features']:
  feature.append(times)
  existingtimes.append (times['properties']['time'])


#---- make lists for time, latitude and longitude from the spot GPS feed ---
count = 0
dataAvailable = True

while dataAvailable:
  try:
    time.append (spotdata["response"]["feedMessageResponse"]["messages"]["message"][count]["dateTime"])
    lat.append (spotdata["response"]["feedMessageResponse"]["messages"]["message"][count]["latitude"])
    lon.append (spotdata["response"]["feedMessageResponse"]["messages"]["message"][count]["longitude"])
    count += 1
  except Exception:
    print("Found " + str(count) + " points from GPS\n")
    dataAvailable = False
    pass


#---- compare times of existing data and new data ----
for oldtime in existingtimes:
  for newtime in time:
    if newtime==oldtime:
      #add the number to the duplicates list
      duplicates.append(time.index(newtime))
print "Found " + str(len(duplicates)) + " Duplicates:\n"



#---- put the time, latitude and longitude together as "features" ----
newData = False
for index in range(len(time)):
  if index not in duplicates: 
    newData = True
    point.append(geojson.Point((lon[index], lat[index])))

    feature.append(geojson.Feature(geometry=point[index], properties={"title": "Vlog 1", "marker-color": "#f86767", "marker-size": "large", "marker-symbol": "star", "url": "https://www.youtube.com/watch?v=ty5Cl9GbbGs", "time": time[index]}))
    print("added feature at time: " + time[index])
if not newData:
  print "\n--- No new data ---\n"


#---- turn the list of features into a collection
collection = geojson.FeatureCollection(feature)


#---- write a geojson file from the collection
with open("datatest.geojson", 'w') as outfile:
  geojson.dump(collection, outfile, sort_keys=True,indent=4, separators=(',', ': '))


pprint(collection)