en#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:29:48 2016

@author: jsrhu
"""

import sys
import os

import pandas as pd

import matplotlib.pyplot as plt

import readWriteData
from stringProcess import removePunctuation

'''
implement scraper for
SPDR:
    SPY
    MDY
Blackrock:
    IWM
'''

'''
create function for general ETF
'''

compressed_data = '../data/csv/backtest_alpha_for_ernest.csv.gz'

etf_path = '../data/etf/'

data_SPY = etf_path+'SPY_All_Holdings.xls'
data_MDY = etf_path+'MDY_All_Holdings.xls'
data_IWM = etf_path+'IWM_holdings.csv'

df_SPY = readWriteData.readToDF(data_SPY)
df_MDY = readWriteData.readToDF(data_MDY)
df_IWM = readWriteData.readToDF(data_IWM)

df_SPY.dropna(inplace=True)
df_MDY.dropna(inplace=True)
df_IWM.dropna(inplace=True)

df_SPY = df_SPY.rename(columns={'Identifier':'Ticker'})
df_MDY = df_MDY.rename(columns={'Identifier':'Ticker'})

df_SPY['Ticker'] = df_SPY['Ticker'].apply(removePunctuation)
df_MDY['Ticker'] = df_MDY['Ticker'].apply(removePunctuation)
df_IWM['Ticker'] = df_IWM['Ticker'].apply(removePunctuation)

count_tickers_SPY = df_SPY['Ticker'].size
count_tickers_MDY = df_MDY['Ticker'].size
count_tickers_IWM = df_IWM['Ticker'].size

date_format="%Y-%m-%d %H:%M:%S %Z"
dateparse = lambda x: pd.datetime.strptime(x, date_format)
rows = 100000
#df_accern = pd.read_csv(filepath_or_buffer=compressed_data, compression='gzip', nrows=rows, header=0, date_parser=dateparse, parse_dates=["harvested_at"])
df_accern = pd.read_csv(filepath_or_buffer=compressed_data, compression='gzip', header=0, date_parser=dateparse, parse_dates=["harvested_at"])
dfgroup_accern = df_accern.groupby( df_accern['harvested_at'].apply(lambda x: x.date() ) )

columns = ['SPY_coverage','MDY_coverage','IWM_coverage']

df_ETF_coverage_average_day = pd.DataFrame(index=dfgroup_accern.indices, columns=columns)

sr_SPY = pd.Series()
sr_MDY = pd.Series()
sr_IWM = pd.Series()

for date,group in dfgroup_accern:
    tickers = group['entities_ticker_1'].unique()
    count_SPY,count_MDY,count_IWM = 0,0,0
    for accern_ticker in tickers:
        if accern_ticker in df_SPY['Ticker'].values:
            count_SPY=count_SPY+1
        if accern_ticker in df_MDY['Ticker'].values:
            count_MDY=count_MDY+1
        if accern_ticker in df_IWM['Ticker'].values:
            count_IWM=count_IWM+1
    coverage_SPY = count_SPY/float(count_tickers_SPY-1)*100
    coverage_MDY = count_MDY/float(count_tickers_MDY-1)*100
    coverage_IWM = count_IWM/float(count_tickers_IWM)*100

    sr_SPY[date] = coverage_SPY
    sr_MDY[date] = coverage_MDY
    sr_IWM[date] = coverage_IWM
    
df_ETF_coverage_average_day['SPY_coverage'] = sr_SPY
df_ETF_coverage_average_day['MDY_coverage'] = sr_MDY
df_ETF_coverage_average_day['IWM_coverage'] = sr_IWM

try:
    output = os.mkdir('output')
except:
    output = 'output'
os.chdir(output)

ax = df_ETF_coverage_average_day.plot(title='ETF Coverage Over Time by Accern Data',rot=45, figsize=(11,8))
ax.set_ylabel('Percentage of ETF')
ax.set_xlabel('Date')
lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.savefig('ETF_coverage'+str(rows)+'rows.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.clf()