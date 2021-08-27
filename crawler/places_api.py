import requests


def google_api_nearby_search(lat, lon, radius, establishment, api_key):
    """
       google_api_nearby_search: search for places within a specified area

       :param lat: lat coordinate of the search center
       :param lon: lon coordinate of the search center
       :param radius: search radius in meter
       :param establishment: like / restaurant / bar / cafe / (night_club / liquor_store)
       :param api_key: api_key (in hidden file)
       :return: json response of all search hits
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="\
          +str(lat)+","+str(lon)+"&radius="+str(radius)+"&type="+str(establishment)+"&key="+str(api_key)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
