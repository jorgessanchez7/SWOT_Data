import geopy
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

# initialize Nominatim API
geopy.geocoders.options.default_user_agent = "my-application"
geolocator = Nominatim(user_agent="name_of_your_app")

'''###---SWOT---###'''

total_swot_stations = pd.read_csv('total_swot_stations_v0.csv')

reach_ids = total_swot_stations['reach_id'].tolist()
xs = total_swot_stations['x'].tolist()
ys = total_swot_stations['y'].tolist()
reach_lens = total_swot_stations['reach_len'].tolist()
widths = total_swot_stations['width'].tolist()
faccs = total_swot_stations['facc'].tolist()
slopes = total_swot_stations['slope'].tolist()
river_names = total_swot_stations['river_name'].tolist()

table = []

for reach_id, x, y, reach_len, width, facc, slope, river_name in zip(reach_ids, xs, ys, reach_lens, widths, faccs, slopes, river_names):

    Latitude = str(y)
    Longitude = str(x)

    try:
        location = geolocator.reverse(Latitude + "," + Longitude, language='en')
        address = location.raw['address']
        country = address.get('country', '')
        print(reach_id, ' - ', river_name, ' - ', country)
    except Exception as e:
        print (e)
        country = np.nan
        print(reach_id, ' - ', river_name, ' - ', country)

    table.append([reach_id, y, x, reach_len, width, facc, slope, river_name, country])

table_df = pd.DataFrame(table, columns=['reach_id', 'Latitude', 'Longitude', 'Reach Length', 'Reach Width', 'Area', 'Slope', 'River Name', 'Country'])

table_df.to_csv('total_swot_stations.csv')

'''###---GEOGloWS---###'''

total_geoglows_streams = pd.read_csv('Total_GEOGloWS_Streams_Data_v0.csv')

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

table_df.to_csv('Total_GEOGloWS_Streams_Data.csv')