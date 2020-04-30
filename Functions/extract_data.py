#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:06:04 2020

@author: florian
"""

def extract():
    '''
    Extract the Open Velib Data with the specific URL provide by the Paris metropole
    Please see documentation here : https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole
    Return a CSV file including the information and status of each velib station
    '''
    import requests
    import datetime
    import pandas as pd
    import numpy as np
    
    # Extract
    dic_infos = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json").json()
    dic_status = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json").json()
    
    #Get the extraction date 
    timestamp = dic_status['lastUpdatedOther']
    
    # 1st dataframe : stations static informations
    df_infos = pd.DataFrame(dic_infos['data']['stations'])
    df_infos['timestamp'] = pd.DataFrame( data = timestamp * np.ones(len(dic_infos['data']['stations'])) , columns=['timestamp']) #add the time at the end
    df_infos['datetime']=  df_infos['timestamp'].apply(lambda x :  str(datetime.datetime.fromtimestamp(x)))
    
    # 2nd dataframe : stations status 
    df_status = pd.DataFrame( dic_status['data']['stations'])
    #splitting the data about the bike types availability : mechanical/ebike
    df_status['mechanical_available'] = df_status['num_bikes_available_types'].apply( lambda x : x[0]['mechanical'])
    df_status['ebike_available'] = df_status['num_bikes_available_types'].apply( lambda x : x[1]['ebike'])
    #dropping the initial column 
    del df_status['num_bikes_available_types']
    
    # merging in one dataframe on 'station_id' and cretaing CSV file 
    df_merge = pd.merge( df_infos, df_status, on = 'station_id')
    df_merge.to_csv(r'Extracts/'+str(timestamp)+'_stations.csv')
    
    print('Velib Data from ' + str(datetime.datetime.fromtimestamp(timestamp))+ ' extracted in a CSV')
    return df_merge #timestamp, str(datetime.datetime.fromtimestamp(timestamp))
