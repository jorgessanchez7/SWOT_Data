import os
import pandas as pd
import geopandas as gpd

folders = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/SWOT/')

df = pd.DataFrame()

for folder in folders:
    #print (folder)
    try:
        subfolders = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/SWOT/{}/'.format(folder))
        #print (subfolders)

        for subfolder in subfolders:
            #print (subfolder)

            files = os.listdir('/Users/grad/Library/CloudStorage/Box-Box/SWOT/{0}/{1}/'.format(folder, subfolder))

            matchers = ['.shp']
            shape_file = [s for s in files if any(xs in s for xs in matchers)]
            shape_file = [file for file in shape_file if '.xml' not in file]
            shape_file = shape_file[0]

            # Path to the shapefile
            shapefile_path = '/Users/grad/Library/CloudStorage/Box-Box/SWOT/{0}/{1}/{2}'.format(folder, subfolder, shape_file)

            # Read the shapefile
            gdf = gpd.read_file(shapefile_path)
            df1 = pd.DataFrame(gdf)
            df1 = pd.DataFrame(gdf.drop(columns=['time', 'time_tai', 'wse_c', 'wse_c_u', 'slope', 'slope_u',
                                                 'slope_r_u', 'slope2', 'slope2_u', 'slope2_r_u', 'width',
                                                 'width_u', 'width_c', 'width_c_u', 'area_total', 'area_tot_u',
                                                 'area_detct', 'area_det_u', 'area_wse', 'd_x_area', 'd_x_area_u',
                                                 'layovr_val', 'node_dist', 'loc_offset', 'xtrk_dist', 'reach_q_b',
                                                 'dark_frac', 'ice_clim_f', 'ice_dyn_f', 'partial_f', 'n_good_nod',
                                                 'obs_frac_n', 'xovr_cal_q', 'geoid_hght', 'geoid_slop', 'solid_tide',
                                                 'load_tidef', 'load_tideg', 'pole_tide', 'dry_trop_c', 'wet_trop_c',
                                                 'iono_c', 'xovr_cal_c', 'n_reach_up', 'n_reach_dn', 'rch_id_up',
                                                 'rch_id_dn', 'p_wse', 'p_wse_var', 'p_width', 'p_wid_var',
                                                 'p_n_nodes', 'p_dist_out', 'p_length', 'p_maf', 'p_dam_id',
                                                 'p_n_ch_max', 'p_n_ch_mod', 'p_low_slp', 'geometry']))

            # Now 'gdf' is a GeoDataFrame that contains all the attributes and geometry data from the shapefile
            #print(df1.head())

            df = pd.concat([df, df1], ignore_index=True)

    except Exception as e:
        print("It is not a folder: {}".format(e))

print(df)

all_dataset = df.to_csv('All_Data.csv')

swot_stations_location = df.copy()
swot_stations_location = swot_stations_location.drop(columns=['time_str', 'wse', 'wse_u', 'wse_r_u', 'dschg_c',
                                                              'dschg_c_u', 'dschg_csf', 'dschg_c_q', 'dschg_gc',
                                                              'dschg_gc_u', 'dschg_gcsf', 'dschg_gc_q', 'dschg_m',
                                                              'dschg_m_u', 'dschg_msf', 'dschg_m_q', 'dschg_gm',
                                                              'dschg_gm_u', 'dschg_gmsf', 'dschg_gm_q', 'dschg_b',
                                                              'dschg_b_u', 'dschg_bsf', 'dschg_b_q', 'dschg_gb',
                                                              'dschg_gb_u', 'dschg_gbsf', 'dschg_gb_q', 'dschg_h',
                                                              'dschg_h_u', 'dschg_hsf', 'dschg_h_q', 'dschg_gh',
                                                              'dschg_gh_u', 'dschg_ghsf', 'dschg_gh_q', 'dschg_o',
                                                              'dschg_o_u', 'dschg_osf', 'dschg_o_q', 'dschg_go',
                                                              'dschg_go_u', 'dschg_gosf', 'dschg_go_q', 'dschg_s',
                                                              'dschg_s_u', 'dschg_ssf', 'dschg_s_q', 'dschg_gs',
                                                              'dschg_gs_u', 'dschg_gssf', 'dschg_gs_q', 'dschg_i',
                                                              'dschg_i_u', 'dschg_isf', 'dschg_i_q', 'dschg_gi',
                                                              'dschg_gi_u', 'dschg_gisf', 'dschg_gi_q', 'dschg_q_b',
                                                              'dschg_gq_b', 'reach_q'])
swot_stations_location.drop_duplicates(subset=['reach_id'], inplace=True)
swot_stations_location = swot_stations_location.to_csv('swot_stations.csv')
