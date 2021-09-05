import json
import pandas as pd


# load data using Python JSON module
with open('../json_files/Json-Answer-Muc-bars.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    print(data)

# Flatten data
df = pd.json_normalize(data, record_path=['elements'])
df = df[['id', 'tags.name', 'lat', 'lon', 'tags.amenity', 'tags.opening_hours', 'tags.website', 'tags.contact:website',
         'tags.website_1', 'tags.website2', 'tags.phone', 'tags.cuisine', 'tags.cuisine_1', 'tags.cuisine_2']]
print(df)
df.info()
df.to_csv(r'C:\Users\nuernie\Desktop\Coding\aps_finder\
            crawler\data_tables\muc_bars_restaurants_cafes.csv')
