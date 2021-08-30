import requests
import json
from config import api_key


class Places:
    """
    Places:
    Is an Google Places API Object for more details have a look at:
    https://developers.google.com/maps/documentation/places/web-service/overview

    functions:
    google_api_nearby_search(): lets you search for places within a specified area
    """

    lat = 0
    lon = 0
    radius = 0
    establishment = ""
    keyword = ""
    next_page_token = ""
    api_key = ""

    def __init__(self, lat, lon, radius, establishment, keyword, next_page_token):
        """
        places_constructor: instantiates the places object

        :param lat: lat coordinate of the search center
        :param lon: lon coordinate of the search center
        :param radius: search radius in meter
        :param establishment: like / restaurant / bar / cafe / (night_club / liquor_store)
        :param keyword: A term to be matched against all content that Google has indexed for this place
        :param next_page_token: leads to the next page if there are more than 20 hits
        """
        self.lat = lat
        self.lon = lon
        self.radius = radius
        self.establishment = establishment
        self.keyword = keyword
        self.next_page_token = next_page_token
        self.api_key = api_key

    def google_api_nearby_search(self):
        """
        google_api_nearby_search: search for places within a specified area
        :return: json response of all search hits only 20 hits will be shown up, next_page_token will guide
                 you to the next search hits as dict.
        """
        # noinspection SpellCheckingInspection
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="\
              + str(self.lat)+","+str(self.lon)+"&radius=" + str(self.radius)+"&type=" + str(self.establishment) + \
              "&keyword=" + str(self.keyword) + "&key=" + str(self.api_key) + "&pagetoken=" + str(self.next_page_token)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.text
        return json.loads(json_response)

    def set_next_page_token(self, next_page_token):
        self.next_page_token = next_page_token

    # TODO add all getters and setters
