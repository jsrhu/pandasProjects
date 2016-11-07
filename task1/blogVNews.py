#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:56:59 2016

@author: jsrhu
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from tqdm import tqdm
matplotlib.style.use('ggplot')
import readWriteData

compressed_data = '../data/csv/backtest_alpha_for_ernest.csv.gz'

df_accern = readWriteData.readToDF(compressed_data)

tqdm.pandas(desc='parsing and grouping by dates')
dfgroup_date = df_accern.groupby(df_accern['harvested_at'].progress_apply(lambda x: x.date()))

#out = dfgroup_date['article_type'].value_counts(normalize=True)

df_counts = pd.DataFrame(columns=['blog','news'])

for key,group in dfgroup_date:
    df_counts['blog'][key] = group['article_type'][ group['article_type'] == 'blog' ].count()
    df_counts['news'][key] = group['article_type'][ group['article_type'] == 'news' ].count()

# have to append df_counts['blog'] and df_counts['news']

df_counts = pd.concat([df_counts['blog'],df_counts['news']], axis=1)
df_counts['total'] = df_counts['news'].add(df_counts['blog'])
df_counts['ratio'] = df_counts['news'].divide(df_counts['blog'])
