from places_api import google_api_nearby_search
from config import api_key

# call google api 
print(google_api_nearby_search(48.150123, 11.575042, 5000, "bar", api_key))
