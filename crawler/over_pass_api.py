import requests
import pandas as pd
import time
import numpy as np


def get_amenity_info(area, amenity_type):
    """
    get_amenity_info: returns information about all amenities
                      in a specific area
    :param area:         str:
                         city
    :param amenity_type: str:
                         bar,restaurant,cafe
    :return pandas dataframe: df    if everything worked fine

    """
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = '[out:json];area[name="'+area+'"];' \
                     'nwr(area)[amenity~"^('+amenity_type+')$"];' \
                     'out center;'
    while True:
        try:
            response = requests.get(overpass_url, params={'data': overpass_query})
            # Check if Server response is 200 = OK for the API call
            print("Server-Code: ", response.status_code)
            if response.status_code != 200:
                if response.status_code == 504:
                    raise Exception("Server-Gateway-Timeout")
                elif response.status_code == 429:
                    raise Exception("Too Many Requests")
                elif response.status_code == 400:
                    raise Exception("Bad Request! Check function Parameters")
                else:
                    raise Exception("Server-Problems try later again!")
            else:
                print("Server: OK!")
                data = response.json()
                # Flatten data and transport to pandas df 
                df = pd.json_normalize(data, record_path=['elements'])
                df = df[['id', 'tags.name', 'lat', 'lon', 'tags.amenity', 'tags.opening_hours', 'tags.website',
                         'tags.contact:website', 'tags.website_1', 'tags.website2', 'tags.phone', 'tags.cuisine',
                         'tags.cuisine_1', 'tags.cuisine_2']]
                return df

        except Exception as e:
            print("Problems occurred !:")
            print(e)
            time.sleep(30)
            continue
        break


def transform_dataset(df):
    df.columns = [
                  'id', 'name', 'lat', 'lon', 'amenity', 'opening_hours', 'website',
                  'contact_website', 'website_1', 'website_2', 'phone', 'cuisine',
                  'cuisine_1', 'cuisine_2'
                  ]
    # df['website'] = df[['website','contact_website','website_1','website_2']].values.tolist()
    # df = df.drop(columns=['contact_website', 'website_1', 'website_2'])

    # df['cuisine'] = df[['cuisine','cuisine_1','cuisine_2']].values.tolist()
    # df = df.drop(columns=['cuisine_1', 'cuisine_2'])

    # aps price add column
    df["aps_price"] = np.nan
    print("")
    print("pandas_df_info: ")
    print("########################################################################################")
    df.info()
    print("########################################################################################")
    df.to_csv('data_tables/muc_bars_restaurants_cafes.csv')
    return df

