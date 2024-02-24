import geopy
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

# initialize Nominatim API
geopy.geocoders.options.default_user_agent = "my-application"
geolocator = Nominatim(user_agent="name_of_your_app")

'''###---SWOT---###'''

total_swot_stations = pd.read_csv('total_swot_stations.csv')

for index, row in total_swot_stations.iterrows():
    latitude = str(row['Latitude'])
    longitude = str(row['Longitude'])
    country = row['Country']

    if pd.isna(country):
        try:
            location = geolocator.reverse(f"{latitude},{longitude}", language='en')
            address = location.raw['address']
            country = address.get('country', '')
            # Update the 'Country' column in the DataFrame
            total_swot_stations.at[index, 'Country'] = country
            print(row['reach_id'], ' - ', row['River Name'], ' - ', row['Country'])
        except Exception as e:
            print(e)
            country = np.nan
            print(row['reach_id'], ' - ', row['River Name'], ' - ', country)
    else:
        print(row['reach_id'], ' - ', row['River Name'], ' - ', country)

total_swot_stations.set_index('reach_id', inplace=True)
total_swot_stations.to_csv('total_swot_stations.csv')

'''###---GEOGloWS---###'''

total_geoglows_streams = pd.read_csv('Total_GEOGloWS_Streams_Data.csv', index_col=0)

for index, row in total_geoglows_streams.iterrows():
    latitude = str(row['Latitude'])
    longitude = str(row['Longitude'])
    country = row['Country']

    if pd.isna(country):
        try:
            location = geolocator.reverse(f"{latitude},{longitude}", language='en')
            address = location.raw['address']
            country = address.get('country', '')
            # Update the 'Country' column in the DataFrame
            total_geoglows_streams.at[index, 'Country'] = country
            print(row['reach_id'], ' - ', row['River Name'], ' - ', row['Country'])
        except Exception as e:
            print(e)
            country = np.nan
            print(row['reach_id'], ' - ', row['River Name'], ' - ', country)
    else:
        print(row['reach_id'], ' - ', row['River Name'], ' - ', country)

total_geoglows_streams.set_index('TDXHydroLi', inplace=True)
total_geoglows_streams.to_csv('Total_GEOGloWS_Streams_Data.csv')