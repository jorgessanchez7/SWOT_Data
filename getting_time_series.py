import pandas as pd

all_data_values = pd.read_csv('/Users/grad/Documents/Github/SWOT/All_Data.csv', index_col=0)
swot_stations_location = pd.read_csv('/Users/grad/Documents/Github/SWOT/swot_stations.csv', index_col=0)

ids = swot_stations_location['reach_id'].to_list()

for id in ids:
    wse_values = all_data_values.copy()
    wse_values = wse_values.drop(columns=['wse_u', 'wse_r_u', 'dschg_c', 'dschg_c_u', 'dschg_csf', 'dschg_c_q',
                                          'dschg_gc', 'dschg_gc_u', 'dschg_gcsf', 'dschg_gc_q', 'dschg_m', 'dschg_m_u',
                                          'dschg_msf', 'dschg_m_q', 'dschg_gm', 'dschg_gm_u', 'dschg_gmsf', 'dschg_gm_q',
                                          'dschg_b', 'dschg_b_u', 'dschg_bsf', 'dschg_b_q', 'dschg_gb', 'dschg_gb_u',
                                          'dschg_gbsf', 'dschg_gb_q', 'dschg_h', 'dschg_h_u', 'dschg_hsf', 'dschg_h_q',
                                          'dschg_gh', 'dschg_gh_u', 'dschg_ghsf', 'dschg_gh_q', 'dschg_o', 'dschg_o_u',
                                          'dschg_osf', 'dschg_o_q', 'dschg_go', 'dschg_go_u', 'dschg_gosf', 'dschg_go_q',
                                          'dschg_s', 'dschg_s_u', 'dschg_ssf', 'dschg_s_q', 'dschg_gs', 'dschg_gs_u',
                                          'dschg_gssf', 'dschg_gs_q', 'dschg_i', 'dschg_i_u', 'dschg_isf', 'dschg_i_q',
                                          'dschg_gi', 'dschg_gi_u', 'dschg_gisf', 'dschg_gi_q', 'dschg_q_b',
                                          'dschg_gq_b', 'reach_q'])
    wse_values = wse_values.loc[wse_values['reach_id'] == id]
    wse_values.set_index('time_str', inplace=True)
    wse_values.to_csv('/Users/grad/Documents/Hydrological_Data/SWOT/Water_Level/{}.csv'.format(id))
    print(wse_values)

    discharge_values = all_data_values.copy()
    discharge_values = discharge_values.drop(columns=['wse', 'wse_u', 'wse_r_u', 'dschg_c_u', 'dschg_csf', 'dschg_c_q',
                                                      'dschg_gc', 'dschg_gc_u', 'dschg_gcsf', 'dschg_gc_q', 'dschg_m_u',
                                                      'dschg_msf', 'dschg_m_q', 'dschg_gm', 'dschg_gm_u', 'dschg_gmsf',
                                                      'dschg_gm_q', 'dschg_b_u', 'dschg_bsf', 'dschg_b_q', 'dschg_gb',
                                                      'dschg_gb_u', 'dschg_gbsf', 'dschg_gb_q', 'dschg_h_u', 'dschg_hsf',
                                                      'dschg_h_q', 'dschg_gh', 'dschg_gh_u', 'dschg_ghsf', 'dschg_gh_q',
                                                      'dschg_o_u', 'dschg_osf', 'dschg_o_q', 'dschg_go', 'dschg_go_u',
                                                      'dschg_gosf', 'dschg_go_q', 'dschg_s_u', 'dschg_ssf', 'dschg_s_q',
                                                      'dschg_gs', 'dschg_gs_u', 'dschg_gssf', 'dschg_gs_q', 'dschg_i_u',
                                                      'dschg_isf', 'dschg_i_q', 'dschg_gi', 'dschg_gi_u', 'dschg_gisf',
                                                      'dschg_gi_q', 'dschg_q_b', 'dschg_gq_b', 'reach_q'])
    discharge_values = discharge_values.loc[discharge_values['reach_id'] == id]
    discharge_values.set_index('time_str', inplace=True)
    discharge_values.to_csv('/Users/grad/Documents/Hydrological_Data/SWOT/Discharge/{}.csv'.format(id))
    print(discharge_values)
