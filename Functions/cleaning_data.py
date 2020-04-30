#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:48:41 2020

@author: florian
"""

def cleaning( file_name ):
    '''
    file_name (string) : name or path of the file 
    Takes the conacatenated CSV file entry and drops duplicated rows and columns
    Creates the new CSV file at the parent directory
    Returns the cleaned dataframe
    '''
    import pandas as pd
    # Import of the data 
    df = pd.read_csv( file_name )
    
    # Dropping the duplicated rows 
    # (with keep= 'first' by default to keep the first occurence)
    df.drop_duplicates( inplace= True)
    
    # Dropping of the first rows containing the column name (from the concatenation of the csv file)
    # (not dropped by the previous method, because of the keep= 'first' parameter)
    df.drop( 
            index =  df[ df['numDocksAvailable'] != df['num_docks_available']].index,
            inplace= True
            )
    
    #Dropping of the duplicated columns 
    df.drop( columns= ['numBikesAvailable', 'numDocksAvailable',  'stationCode_y'], inplace= True  )
    
    #Creating the new file with cleaned data at parent directory
    import pathlib
    df.to_csv( str( pathlib.Path.cwd().parent) + '/cleanedData.csv' )
    
    return df 