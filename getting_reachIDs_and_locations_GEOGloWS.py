import os
import pandas as pd
import geopandas as gpd

'''vpu 600'''
###vpu 600###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_600_Shapefile')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_600_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df6 = pd.DataFrame(gdf)

    df6 = pd.DataFrame(df6.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df6], ignore_index=True)

#print(df)

geoglows_streams_location6 = df.copy()

geoglows_streams_location6.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location6.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location6.sort_values(by=['VPUCode'])
geoglows_streams_location6.to_csv('vpu_600_GEOGloWS_Streams_Data.csv')

'''vpu 100'''
###vpu 100###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_100_Shapefile/')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_100_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df1 = pd.DataFrame(gdf)

    df1 = pd.DataFrame(df1.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df1], ignore_index=True)

#print(df)

geoglows_streams_location1 = df.copy()

geoglows_streams_location1.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location1.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location1.sort_values(by=['VPUCode'])
geoglows_streams_location1.to_csv('vpu_100_GEOGloWS_Streams_Data.csv')

'''vpu 200'''
###vpu 200###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_200_Shapefile')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_200_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df2 = pd.DataFrame(gdf)

    df2 = pd.DataFrame(df2.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df2], ignore_index=True)

#print(df)

geoglows_streams_location2 = df.copy()

geoglows_streams_location2.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location2.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location2.sort_values(by=['VPUCode'])
geoglows_streams_location2.to_csv('vpu_200_GEOGloWS_Streams_Data.csv')

'''vpu 300'''
###vpu 300###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_300_Shapefile/')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_300_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df3 = pd.DataFrame(gdf)

    df3 = pd.DataFrame(df3.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df3], ignore_index=True)

#print(df)

geoglows_streams_location3 = df.copy()

geoglows_streams_location3.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location3.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location3.sort_values(by=['VPUCode'])
geoglows_streams_location3.to_csv('vpu_300_GEOGloWS_Streams_Data.csv')

'''vpu 400'''
###vpu 400###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_400_Shapefile')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_400_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df4 = pd.DataFrame(gdf)

    df4 = pd.DataFrame(df4.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df4], ignore_index=True)

#print(df)

geoglows_streams_location4 = df.copy()

geoglows_streams_location4.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location4.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location4.sort_values(by=['VPUCode'])
geoglows_streams_location4.to_csv('vpu_400_GEOGloWS_Streams_Data.csv')

'''vpu 500'''
###vpu 500###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_500_Shapefile/')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_500_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df5 = pd.DataFrame(gdf)

    df5 = pd.DataFrame(df5.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df5], ignore_index=True)

#print(df)

geoglows_streams_location5 = df.copy()

geoglows_streams_location5.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location5.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location5.sort_values(by=['VPUCode'])
geoglows_streams_location5.to_csv('vpu_500_GEOGloWS_Streams_Data.csv')

'''vpu 700'''
###vpu 700###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_700_Shapefile/')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_700_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df7 = pd.DataFrame(gdf)

    df7 = pd.DataFrame(df7.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df7], ignore_index=True)

#print(df)

geoglows_streams_location7 = df.copy()

geoglows_streams_location7.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location7.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location7.sort_values(by=['VPUCode'])
geoglows_streams_location7.to_csv('vpu_700_GEOGloWS_Streams_Data.csv')

'''vpu 800'''
###vpu 800###

files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_800_Shapefile')

matchers = ['.shp']
shape_files = [s for s in files if any(xs in s for xs in matchers)]
shape_files = [file for file in shape_files if '.xml' not in file]
shape_files = sorted(shape_files)

df = pd.DataFrame()

for shape_file in shape_files:

    print(shape_file)

    # Path to the shapefile
    shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/GEOGloWS/GEOGloWS_v2.0/Streams_v2/vpu_800_Shapefile/{0}'.format(shape_file)

    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    df8 = pd.DataFrame(gdf)

    df8 = pd.DataFrame(df8.drop(columns=['fid', 'LINKNO', 'DSLINKNO', 'DSNODEID', 'strmDrop', 'Slope', 'StraightL', 'WSNO', 'DOUTEND',
                                         'DOUTSTART', 'DOUTMID', 'z', 'TDXHydroRe', 'Topologica', 'musk_k', 'musk_x', 'velocity_f',
                                         'CountUS', 'USLINKNO1', 'USLINKNO2', 'USLINKNO3', 'TerminalNo', 'USLINKNO4', 'geometry']))

    df = pd.concat([df, df8], ignore_index=True)

#print(df)

geoglows_streams_location8 = df.copy()

geoglows_streams_location8.drop_duplicates(subset=['TDXHydroLi'], inplace=True)
geoglows_streams_location8.set_index('TDXHydroLi', inplace=True)
geoglows_streams_location8.sort_values(by=['VPUCode'])
geoglows_streams_location8.to_csv('vpu_800_GEOGloWS_Streams_Data.csv')