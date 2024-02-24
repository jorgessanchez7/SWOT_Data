import geopy
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

# initialize Nominatim API
geopy.geocoders.options.default_user_agent = "my-application"
geolocator = Nominatim(user_agent="name_of_your_app")

'''###---GEOGloWS---###'''

total_geoglows_streams = pd.read_csv('vpu_100_GEOGloWS_Streams_Data_v0.csv')

TDXHydroLis = total_geoglows_streams['TDXHydroLi'].tolist()
strmOrders = total_geoglows_streams['strmOrder'].tolist()
Lengths = total_geoglows_streams['Length'].tolist()
Magnitudes = total_geoglows_streams['Magnitude'].tolist()
DSContAreas = total_geoglows_streams['DSContArea'].tolist()
USContAreas = total_geoglows_streams['USContArea'].tolist()
LengthGeods = total_geoglows_streams['LengthGeod'].tolist()
lats = total_geoglows_streams['lat'].tolist()
lons = total_geoglows_streams['lon'].tolist()
VPUCodes = total_geoglows_streams['VPUCode'].tolist()

table = []

for TDXHydroLi, strmOrder, Length, Magnitude, DSContArea, USContArea, LengthGeod, lat, lon, VPUCode in zip(TDXHydroLis, strmOrders, Lengths, Magnitudes, DSContAreas, USContAreas, LengthGeods, lats, lons, VPUCodes):

    Latitude = str(lat)
    Longitude = str(lon)

    try:
        location = geolocator.reverse(Latitude + "," + Longitude, language='en')
        address = location.raw['address']
        country = address.get('country', '')
        if country == 'United States':
            country = 'Unitated States of America'
        elif country == "Côte d'Ivoire":
            country = 'Ivory Coast'
        else:
            country = country
        print(TDXHydroLi, ' - ', VPUCode, ' - ', country)
    except Exception as e:
        print (e)
        country = np.nan
        print(TDXHydroLi, ' - ', VPUCode, ' - ', country)

    table.append([TDXHydroLi, strmOrder, Length, Magnitude, DSContArea, USContArea, LengthGeod, lat, lon, VPUCode, country])

table_df = pd.DataFrame(table, columns=['TDXHydroLi', 'strmOrder', 'Length', 'Magnitude', 'DSContArea', 'USContArea', 'LengthGeod', 'Latitude', 'Longitude', 'VPUCode', 'Country'])
table_df.set_index('TDXHydroLi', inplace=True)

table_df.to_csv('vpu_100_GEOGloWS_Streams_Data.csv')