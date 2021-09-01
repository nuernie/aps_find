import traceback
import requests
import json
import sys
import pandas as pd


# load data using Python JSON module
with open('Json-Answer-Muc-bars.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    print(data)

# Flatten data
df_nested_list = pd.json_normalize(data,record_path = ['elements'])

print(df_nested_list['tags.opening_hours'])

print(df_nested_list)
df_nested_list.info()
df_nested_list.to_csv('muc_bars.csv')

