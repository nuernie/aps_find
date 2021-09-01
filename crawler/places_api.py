import traceback

import requests
import json
import sys
import pandas as pd

# TODO bei Serverproblemen neue starten nach zeit ablauf !
# TODO Overpass API Limits abchecken
# http://overpass-api.de/api/interpreter?data=[out:json];area[name="München"];nwr(area)[amenity~"^(bar|cafe|pub|restaurant)$"];out center;
# {} dict in python / Zugriff .get("")
# [] list in python / Zugriff [0]

struct = {}
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area[name="München"];
nwr(area)[amenity~"^(bar|cafe|pub|restaurant)$"];
out center;
"""

try:
    response = requests.get(overpass_url, params={'data': overpass_query})
    # Check if Server response is 200 = OK for the API call
    print("Server-Code: ", response.status_code)
    if(response.status_code != 200):
        if(response.status_code == 504):
            print("Server-Gateway-Timeout")
            sys.exit()
        elif(response.status_code == 429):
            print("Too Many Requests")
            sys.exit()
        else:
            print("Server-Problems try later again!")
            sys.exit()
    else:
        data = response.json()
        # Flatten data and transport to pandas df
        df = pd.json_normalize(data, record_path=['elements'])
        df = df[['id', 'tags.name', 'lat', 'lon', 'tags.amenity', 'tags.opening_hours', 'tags.website',
                 'tags.contact:website','tags.website_1', 'tags.website2', 'tags.phone', 'tags.cuisine',
                 'tags.cuisine_1', 'tags.cuisine_2']]
        print(df)
        df.info()
        df.to_csv('data_tables/muc_bars.csv')


except Exception as e:
    print("Unkown Failure is occured See Error Message!:")
    print(e)



