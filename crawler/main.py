from places_api import google_api_nearby_search
from config import api_key

# call google api 
print(google_api_nearby_search(48.14955389397138, 11.581264850051875, 5000, "", api_key))
