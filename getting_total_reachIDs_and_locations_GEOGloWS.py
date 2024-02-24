import os
import pandas as pd
import geopandas as gpd

folders = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/')
matcher = ['_Shapefile']
folders = [s for s in folders if any(xs in s for xs in matcher)]
folders = sorted(folders)

df = pd.DataFrame()

for folder in folders:
    print (folder)

    files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/{0}'.format(folder))

    matchers = ['.shp']
    shape_files = [s for s in files if any(xs in s for xs in matchers)]
    shape_files = [file for file in shape_files if '.xml' not in file]
    shape_files = sorted(shape_files)

    for shape_file in shape_files:

        print(shape_file)

        # Path to the shapefile
        shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/{0}/{1}'.format(folder, shape_file)

        # Read the shapefile
        gdf = gpd.read_file(shapefile_path)
        df1 = pd.DataFrame(gdf)

        df1 = pd.DataFrame(df1.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND', 'DOUTSTART',
                                             'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f', 'CountUS', 'USLINKNO1',
                                             'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

        df = pd.concat([df, df1], ignore_index=True)


#print(df)

geoglows_streams_location = df.copy()

geoglows_streams_location.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location.sort_values(by=['VPUCode'])
geoglows_streams_location = geoglows_streams_location.to_csv('Total_GEOGloWS_Streams_Data_v0.csv')