#A way to run a server using virtualbox -> connect to raspberry pi

import os
import json
import urllib

#url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal%20Studios%20Hollywood&mode=walking&key=AIzaSyBfFAGyGioO5PDmoOmF-G_7RT6pV8AtR8o'
url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBfFAGyGioO5PDmoOmF-G_7RT6pV8AtR8o'

jsonURL = urllib.urlopen(url)
json_data = json.loads(jsonURL.read())       #Stores entire JSON object fetched from the REST endpoint
json_data = json_data.get('routes')[0]
json_data = json_data['legs'][0]
with open('test_json.json', 'w') as write_file:
    json.dump(json_data, write_file, indent=2)

# with open('directions_json.json', 'w') as write_file:
#     json.dump(json_data, write_file, indent=2)
#
# all_steps = json_data['steps']
# for step in all_steps:
#     start_location = step['start_location']
#     # print(start_location)
#     lat = start_location['lat']
#     long = start_location['lng']
#     try:
#         maneuver = step['maneuver']
#     except:
#         maneuver = ""
#     print(lat)
#     print(long)
#     print(maneuver)
