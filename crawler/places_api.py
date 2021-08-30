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
          +str(lat)+","+str(lon)+"&radius="+str(radius)+"&type="+str(establishment)+"&keyword=bar and restaurant and cafe&key="+str(api_key)+"&pagetoken=Aap_uEDvLXdXx7oQNHJh70otDmgY3D7DLrwIFS7In_EazXINmq85ZVKh83Hc4qvNpQOCEtO3yadWTDD6hV-i0if2JwTFCEevvlMwK6hl6LXis9W4WoOevMY5l8VzANscL6nbGzz90PXEs3UEyE2Ap4HIJaSRCjHLO6k6DYbAMD-i2m4FwnMI0aaU5Ajh1Emk9xrN-Nq9MVwq0zIkM8NRKRQF4KC6RFoI-z_daLV7CPccLI3XzB0AjUjsR3QWjIVhb1gD8C5E1c9X_65ZgyHCz7y-2G_ZWA81A-kFk4oqfrcxZf8gOCQzTphOAdhonOoOY_LrN_YmqRhRDVG_J-yIjywo4QBo5FHb37O2dJ3Pftv74zZSkEr-qe0dud42Nl7q-7s1Gt5eQ1r7bZ3pA1T0eJmk7-3rTPjD1WFvLOVHHs5L6b1tPDhTevxRiDwEgZnCk3FmdRMstqysaFkNvquLrJ0"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
