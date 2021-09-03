import requests
import pandas as pd


def get_amenity_info(area, amenity_type):
    """
    get_amenity_info: returns information about all amenities
                      in a specific area
    :param area:         str:
                         city
    :param amenity_type: str:
                         bar,restaurant,cafe
    :return pandas dataframe: df    if everything worked fine
                         int: -1    if something went wrong
    """
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = '[out:json];area[name="'+area+'"];' \
                     'nwr(area)[amenity~"^('+amenity_type+')$"];' \
                     'out center;'
    try:
        response = requests.get(overpass_url, params={'data': overpass_query})
        # Check if Server response is 200 = OK for the API call
        print("Server-Code: ", response.status_code)
        if response.status_code != 200:
            if response.status_code == 504:
                print("Server-Gateway-Timeout")
                return -1
            elif response.status_code == 429:
                print("Too Many Requests")
                return -1
            elif response.status_code == 400:
                print("Bad Request! Check function Parameters")
                return -1
            else:
                print("Server-Problems try later again!")
                return -1
        else:
            print("Server: OK!")
            data = response.json()
            # Flatten data and transport to pandas df
            df = pd.json_normalize(data, record_path=['elements'])
            df = df[['id', 'tags.name', 'lat', 'lon', 'tags.amenity', 'tags.opening_hours', 'tags.website',
                     'tags.contact:website', 'tags.website_1', 'tags.website2', 'tags.phone', 'tags.cuisine',
                     'tags.cuisine_1', 'tags.cuisine_2']]
            print("")
            print("pandas_df_info: ")
            print("########################################################################################")
            df.info()
            print("########################################################################################")
            df.to_csv('data_tables/muc_bars_restaurants_cafes.csv')
            return df

    except Exception as e:
        print("Unknown Failure see Error Message!:")
        print(e)
        return -1
