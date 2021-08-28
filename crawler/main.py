from places_api import Places

# TODO clean all the shit up and itterate trough all the result pages if there more than 20 hits

# safe json answer as file
# with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(json_response, f, ensure_ascii=False, indent=4)
# load json data from file to economize api calls
# with open('data.json') as f:
#    json_response = json.load(f)

# Create a Places Object
place = Places(48.150342454, 11.5759139050, 2000, "", "bar and cafe and restaurant", "")


# idea
# check if there is a next_page
# if yes start the loop again with new data
"""
def update_data():
    print("updating api stream in case of next page")
    try:
        print(data["next_page_token"])
        print("There is one more page!")
        next_page_token = data["next_page_token"]
        next_page_flag = 1
    except:
        print("there are no other pages")
        next_page_flag = -1


if(next_page_flag == 1):
    update_data()
"""

# results loop
for res in place.google_api_nearby_search()["results"]:
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
        print("business_status: ",res["business_status"])
    except:
        print("business_status is not accessible")
    try:
        print("places_id: ",res["place_id"])
    except:
        print("place_id is not accessible")
    try:
        print("rating",res["rating"])
    except:
        print("rating is not accessible")
    try:
        print("uer_rating_total: ",res["user_ratings_total"])
    except:
        print("user_rating_total is not accessible")
    try:
        print("opening_hours: ",res["opening_hours"])
    except:
        print("opening_hours are not accessible")

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
