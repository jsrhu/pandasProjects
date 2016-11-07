#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:07:59 2016

@author: jsrhu
"""
import numpy as np
import pandas as pd
from urlparse import urlparse
from tqdm import tqdm

import cPickle

import readWriteData

compressed_data = '../data/csv/backtest_alpha_for_ernest.csv.gz'
'''
print 'reading data frame'
# try to check for pickle to reduce read time
df_accern = readWriteData.readToDF(compressed_data)

print 'replacing string "na" with np.Nan in "overall_source_rank"'
df_accern['overall_source_rank'] = df_accern['overall_source_rank'].replace(to_replace='na',value=np.nan)

tqdm.pandas(desc="grouping by article domain")
df_accern['article_url'] = df_accern['article_url'].progress_apply( lambda x: str(urlparse(str(x)).netloc))
dfgroup_domain = df_accern.groupby(df_accern['article_url'])


print ''
print 'creating new df'
df_sourcerank = pd.DataFrame()

tqdm.pandas(desc="maximum article domain rank")
df_sourcerank['max'] = dfgroup_domain['overall_source_rank'].progress_apply(lambda x: x.max())
print df_sourcerank['max']

tqdm.pandas(desc="minimum article domain rank")
df_sourcerank['min'] = dfgroup_domain['overall_source_rank'].progress_apply(lambda x: x.min())
print df_sourcerank['min']

tqdm.pandas(desc="median article domain rank")
df_sourcerank['median'] = dfgroup_domain['overall_source_rank'].progress_apply(lambda x: x.median())
print df_sourcerank['median']

tqdm.pandas(desc="mean article domain rank")
#for full set check for Nan values
df_sourcerank['mean'] = dfgroup_domain['overall_source_rank'].progress_apply(lambda x: float(x.mean()))
print df_sourcerank['mean']
'''
df_sourcerank = cPickle.load(open("../data/pickle/df_sourcerank.pickle" ,"rb"))
print 'drop nan'
df_sourcerank = df_sourcerank.dropna()
print 'sorting'
df_sourcerank = df_sourcerank.sort_values(by='mean')

df_sourcerank_high = df_sourcerank.tail(100)
print 'high source rank:'
print df_sourcerank_high

df_sourcerank_low = df_sourcerank.head(100)
print 'low source rank:'
print df_sourcerank_low

print 'high and low to csv'
df_sourcerank_high.to_csv('../output/sourcerank_high.csv')
df_sourcerank_low.to_csv('../output/sourcerank_low.csv')

print 'pickling source rank'
readWriteData.pickleDF(df_sourcerank, 'sourcerank')
