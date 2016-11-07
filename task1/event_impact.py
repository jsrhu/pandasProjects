#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:41:15 2016

@author: jsrhu
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import cPickle
from tqdm import tqdm
from urlparse import urlparse

import readWriteData

compressed_data = '../data/csv/backtest_alpha_for_ernest.csv.gz'
'''
print 'loading pickle'
df_aggregate = cPickle.load(open('../data/pickle/df_aggregate.pickle','rb'))
'''
print 'reading data frame'
# try to check for pickle to reduce read time
df_accern = readWriteData.readToDF(compressed_data)

df_impact = df_accern[['article_url','event_impact_score_entity_1','harvested_at']]

print 'remove records earlier than 01/09/14'
df_impact = df_impact[df_impact['harvested_at'] > datetime(2014,9,1)]

print 'drop nan'
df_impact = df_impact.dropna()

tqdm.pandas(desc="grouping by article domain")
df_impact['article_url'] = df_impact['article_url'].progress_apply( lambda x: str(urlparse(str(x)).netloc))
dfgroup_domain_impact = df_impact.groupby(df_impact['article_url'])

df_impact_final = pd.DataFrame()

tqdm.pandas(desc="maximum article event impact")
df_impact_final['max_event_impact_score_entity_1'] = dfgroup_domain_impact['event_impact_score_entity_1'].progress_apply(lambda x: x.max())

tqdm.pandas(desc="minimum article domain rank")
df_impact_final['min_event_impact_score_entity_1'] = dfgroup_domain_impact['event_impact_score_entity_1'].progress_apply(lambda x: x.min())

tqdm.pandas(desc="median article domain rank")
df_impact_final['median_event_impact_score_entity_1'] = dfgroup_domain_impact['event_impact_score_entity_1'].progress_apply(lambda x: x.median())

tqdm.pandas(desc="mean article domain rank")
df_impact_final['mean_event_impact_score_entity_1'] = dfgroup_domain_impact['event_impact_score_entity_1'].progress_apply(lambda x: float(x.mean()))
