#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:52:20 2016

@author: jsrhu
"""

from pandas.io.json import json_normalize

import json

from tqdm import tqdm

import os
import sys

# have to iterate through dir
path = './data/json/AccernData/test.json'

with open(path,'rb') as f:
        data_test = json.load(f)
        df_test = json_normalize(data=data_test)

print df_test.dtypes

tqdm.pandas(desc='gather primary tickers')
df_test['entities_ticker_1'] = df_test['entities'].progress_apply(lambda x: x[0]['ticker'])
#ticker2
#tqdm.pandas(desc='gather secondary tickers')
#df_test['ticker2'] = df_test['entities'].progress_apply(lambda x: x[1]['ticker'])

tqdm.pandas(desc='gather primary sectors')
df_test['entities_sector_1'] = df_test['entities'].progress_apply(lambda x: x[0]['sector'])
#ticker2
#tqdm.pandas(desc='gather secondary sectors')
#df_test['sector2'] = df_test['entities'].progress_apply(lambda x: x[1]['sector'])

tqdm.pandas(desc='gather event impact on primary tickers')
df_test['event_impact_score_entity_1'] = df_test['event_impact_score.on_entities'].progress_apply(lambda x: x[0]['on_entity'])
#ticker2
#tqdm.pandas(desc='gather event impact on secondary tickers')
#df_test['impact2'] = df_test['event_impact_score.on_entities'].progress_apply(lambda x: x[1]['on_entity'])

print df_test[['harvested_at','entities_ticker_1', 'entities_sector_1','event_impact_score_entity_1','article_sentiment','overall_source_rank']]
