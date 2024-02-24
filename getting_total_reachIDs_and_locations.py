import os
import pandas as pd
import geopandas as gpd

folders = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/SWOT/SWOT_Prior_River_Database_-_SWORD/')

df = pd.DataFrame()

for folder in folders:
    print (folder)
    try:
        files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/SWOT/SWOT_Prior_River_Database_-_SWORD/{}/'.format(folder))
        #print (subfolders)

        matchers = ['.shp']
        shape_file = [s for s in files if any(xs in s for xs in matchers)]
        shape_file = [file for file in shape_file if '.xml' not in file]
        shape_file = shape_file[0]

        # Path to the shapefile
        shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/SWOT/SWOT_Prior_River_Database_-_SWORD/{0}/{1}'.format(folder, shape_file)

        # Read the shapefile
        gdf = gpd.read_file(shapefile_path)
        df1 = pd.DataFrame(gdf)

        df1 = pd.DataFrame(gdf.drop(columns=['n_nodes', 'wse', 'wse_var', 'width_var', 'n_chan_max', 'n_chan_mod',
                                             'obstr_type', 'grod_id', 'hfalls_id', 'dist_out', 'lakeflag', 'max_width',
                                             'n_rch_up', 'n_rch_dn', 'rch_id_up', 'rch_id_dn', 'swot_orbit', 'swot_obs',
                                             'type', 'edit_flag', 'trib_flag', 'geometry']))

        df = pd.concat([df, df1], ignore_index=True)

    except Exception as e:
        print("It is not a folder: {}".format(e))


#print(df)

swot_stations_location = df.copy()

swot_stations_location.drop_duplicates(subset=['reach_id'], inplace=True)
swot_stations_location.set_index('reach_id', inplace=True)
swot_stations_location = swot_stations_location.to_csv('total_swot_stations_v0.csv')

df.set_index('reach_id', inplace=True)
all_dataset = df.to_csv('Total_SWOT_Data.csv')