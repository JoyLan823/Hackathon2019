import os
import json
import urllib

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal%20Studios%20Hollywood&mode=walking&key=AIzaSyBfFAGyGioO5PDmoOmF-G_7RT6pV8AtR8o'

jsonURL = urllib.urlopen(url)
json_data = json.loads(jsonURL.read())       #Stores entire JSON object fetched from the REST endpoint
print (json_data)
with open('directions_json.json', 'w') as write_file:
    json.dump(json_data, write_file, indent=2)
