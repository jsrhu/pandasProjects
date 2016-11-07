#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:43:24 2016

@author: jsrhu
"""
import pandas as pd
import matplotlib.pyplot as plt
from task1 import readLimitedRows

compressed_data = '../data/csv/backtest_alpha_for_ernest.csv.gz'
rows = 1

df = readLimitedRows(csv_file=compressed_data,rows=rows)

array = [x for x in range(10)]
         
series = pd.Series(array)

series.hist(bins=[0,2,10])