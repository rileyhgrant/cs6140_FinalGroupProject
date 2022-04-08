import numpy as np
import pandas as pd
import matplotlib as matplotlib

import json


# cigarette minor cleaning and renaming

clean_cig_df = pd.read_csv('data/clean_cigarette.csv')
cig_to_drop = [
    'county_short',
    'state_abbrev',
    '2005_cig_total',
    '2005_cig_daily',
    '2006_cig_total',
    '2006_cig_daily',
    '2007_cig_total',
    '2007_cig_daily',
    '2008_cig_total',
    '2008_cig_daily',
    '2009_cig_total',
    '2009_cig_daily',
    '2010_cig_total',
    '2010_cig_daily',
    '2011_cig_total',
    '2011_cig_daily',
    'county_full',
    'state_full'
]
clean_cig_df_only_2012 = clean_cig_df.drop( cig_to_drop, axis=1, inplace=False )

clean_cig_df_only_2012.rename(columns = {
    '2012_cig_daily' : 'cig_daily_2012',
    '2012_cig_total' : 'cig_total_2012'
}, inplace=True)


print(clean_cig_df_only_2012.head())



# alcohol minor cleaning and renaming

clean_alc_df = pd.read_csv('data/clean_alcohol.csv')
alc_to_drop = [
    'Unnamed: 0',
    'State',
    'Location',
    '2005 any', '2005 heavy', '2005 binge',
    '2006 any', '2006 heavy', '2006 binge',
    '2007 any', '2007 heavy', '2007 binge',
    '2008 any', '2008 heavy', '2008 binge',
    '2009 any', '2009 heavy', '2009 binge',
    '2010 any', '2010 heavy', '2010 binge',
    '2011 any', '2011 heavy', '2011 binge',
]
clean_alc_df_only_2012 = clean_alc_df.drop( alc_to_drop, axis=1, inplace=False )

clean_alc_df_only_2012.rename(columns = {
    '2012 any'   : 'alc_any_2012',
    '2012 heavy' : 'alc_heavy_2012',
    '2012 binge' : 'alc_binge_2012',
}, inplace=True)

print(clean_alc_df_only_2012.head())


# current joined table, minor cleaning and renaming

curr_join_df = pd.read_csv('data/CountyState_Alc_Cig_HDDeath.csv')

curr_join_df.drop( ['2012 Both Sexes', 'cig_total_mean', 'cig_daily_mean'], axis=1, inplace=True)
curr_join_df.rename(columns = {
    'deaths-per-100k' : 'hd_deaths_per100k_over65'
}, inplace=True)

print(curr_join_df.head())

intermed_df = clean_cig_df_only_2012.join( clean_alc_df_only_2012.set_index( 'county_state' ), on="county_state" )
final_df = intermed_df.join( curr_join_df.set_index( 'county_state'), on="county_state");
# final_df = clean_cig_df.join( clean_alc_df.set_index( 'county_state' ), on="county_state" )
# print(final_df.head())

final_df.to_csv('data/data_full.csv', index = False)


