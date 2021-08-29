from places_api import Places
import time

# TODO alles in eine fancy funktion packen den status der requests auch noch abfragen
# TODO OK , INVALID_REQUEST / {'html_attributions': [], 'results': [], 'status': 'INVALID_REQUEST'}


def get_places_results(place_obj):
    # results loop
    try:
        data_response = place_obj.google_api_nearby_search()["results"]
    except:
        print("there no results!")

    for res in data_response:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        try:
            print("name:", res["name"])
        except:
            print("name is not accessible")
        try:
            print("location: ", res["geometry"]["location"])
        except:
            print("location is not accessible")
        try:
            print("business_status: ", res["business_status"])
        except:
            print("business_status is not accessible")
        try:
            print("places_id: ", res["place_id"])
        except:
            print("place_id is not accessible")
        try:
            print("rating", res["rating"])
        except:
            print("rating is not accessible")
        try:
            print("uer_rating_total: ", res["user_ratings_total"])
        except:
            print("user_rating_total is not accessible")
        try:
            print("opening_hours: ", res["opening_hours"])
        except:
            print("opening_hours are not accessible")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    while (True):
        try:
            print(place_obj.google_api_nearby_search()["next_page_token"])
            print("There is one more page!")
            next_page_token = place_obj.google_api_nearby_search()["next_page_token"]
            place_obj.set_next_page_token(next_page_token)
            time.sleep(5)
            get_places_results(place_obj)
        except:
            print("there are no other pages")
            break;




# Create a Places Object
#TODO mit Kreisen die ganze Fläche abdecken + type restaurant / bar / caffee alles durchsuchen!
#TODO Schnittmengen bei duplikaten rauswerfen!

place = Places(48.150342454, 11.5759139050, 200, "restaurant", "", "")
get_places_results(place)




