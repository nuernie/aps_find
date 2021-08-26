import requests

# function description
def get_json_response(lat, lon, radius, establishment, api_key):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(lat)+","+str(lon)+"&radius="+str(radius)+"&type="+str(establishment)+"&key="+str(api_key)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)