#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:04:56 2016

@author: jsrhu

Library for general pandas DataFrame creation

TODO
add specifiers
"""

import pandas as pd

def readCSV(data_path):
    df = pd.read_csv(data_path, header=10)
    return df
    
def readJSON(data_path):
    df = pd.read_json(data_path)
    return df
    
def readXLS(data_path):
    df = pd.read_excel(data_path, skiprows=3)
    return df

'''
placed here so functions are defined in dict
'''
dict_type = {'csv':readCSV,
             'json':readJSON,
             'xls':readXLS}

def readToDF(data_path):
    data_type = data_path.split('.')
    '''
    index third element of data_type ['','','/data/foo/bar/','file_extension']
    '''
    df = dict_type[data_type[3]](data_path=data_path)
    return df