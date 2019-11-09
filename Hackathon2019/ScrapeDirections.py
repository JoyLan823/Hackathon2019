import os
import json
import urllib

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal%20Studios%20Hollywood&mode=walking&key=YOURKEY'

jsonURL = urllib.urlopen(url)
json_data = json.loads(jsonURL.read())       #Stores entire JSON object fetched from the REST endpoint
json_data = json_data.get('routes').get('legs')
with open('directions_json.json', 'w') as write_file:
    json.dump(json_data, write_file, indent=2)
