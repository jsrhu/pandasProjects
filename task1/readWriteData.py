#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:04:56 2016

@author: jsrhu

Library for general pandas DataFrame creation

TODO
add specifiers
"""
import os

import numpy as np
import cPickle
import pandas as pd

dir_pickle = '../data/pickle/'

'''
based on CSV files from SPDR: header=10
'''
def readCSV(path_data):
    date_format="%Y-%m-%d %H:%M:%S %Z"
    dateparse = lambda x: pd.datetime.strptime(x, date_format)
    df = pd.read_csv(str(path_data), header=0, dtype={'overall_source_rank':np.float64,'event_impact_score_entity_1':np.float64}, na_values=['na'], date_parser=dateparse, parse_dates=["harvested_at"])#, chunksize=10000)#, nrows=1000000)
    return df

'''
based on JSON from Accern
'''
def readJSON(path_data):
    df = pd.read_json(str(path_data))
    return df

'''
based on XLS from Blackrock
'''
def readXLS(path_data):
    df = pd.read_excel(str(path_data, skiprows=3))
    return df

'''
generalized read to df function
'''
def readToDF(path_data):
    if not os.path.exists(str(path_data)):
        print 'File not found: check the file path'
        return
    
    dict_type = {'csv':readCSV,
             'json':readJSON,
             'xls':readXLS}
    
    file_ = os.path.basename(path_data).split('.')
    file_extension = file_[1]

    df = dict_type[file_extension](path_data=path_data)
    
    return df

def pickleDF(df,name):
    name = str(name)
    file_name = 'df_'+name+'.pickle'
    try:
        os.mkdir(dir_pickle)
    except:
        pass
    if os.path.exists(dir_pickle+file_name):
        # update pickle or retrieve old pickle?
        print 'Pickle exists: retrieving pickle'
        return returnPickle(name)
    else:
        print 'Creating pickle'
        with file(dir_pickle+file_name, 'wb') as f:
            return cPickle.dump(df, f)
    
def returnPickle(name):
    name = str(name)
    file_name = dir_pickle+'df_'+name+'.pickle'
    print file_name
    with open(file_name,'rb') as f:
        try:
            return cPickle.load(f)
        except:
            print 'Error'