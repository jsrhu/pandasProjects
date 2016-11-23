#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////

lib.function.py
Created on Tuesday Nov 22 12:31 2016
@author: jsrhu

LIBRARY FILE

////////////////////////////////////////////////
------------------------------------
Packages
------------------------
STDLIB:

MAINTAINED:
pandas

CUSTOM:
readWriteData
directory
parsers

------------------------------------
Constants
------------------------
Integers: int
------------

------------------------
Long: long
------------

------------------------
Floats: float
------------

------------------------
Complex: complex
------------

------------------------
Strings: str
------------

------------------------
Arrays: list
------------

------------------------
Tuple: (x,y)
------------

------------------------
Sets: set
------------

------------------------
Frozen Set: frozenset
------------

------------------------
Dictionary: {'x':x,'y':y}
------------

------------------------------------
Functions
------------------------
Public
------------
AccernFilter

------------------------
Private
------------
_dayAvg

////////////////////////////////////////////

TODO:
Implement function filters

////////////////////////////////////////////////
"""
import pandas as pd

import readWriteData as rwd
import directory as dr
import parsers as prs

def AccernFilter(data = ''):
    df = rwd.readToDF(str(data))
    return df

def domainFrequency(data = pd.DataFrame()):
    pass

def _dayAvg(data = pd.DataFrame()):
    df_avg_day = pd.DataFrame(columns=['dofm','total','day_avg'])
    sr_dofm = pd.Series()

    list_url = []
    for date,row in df_group['article_url']:
        for url in row:
            domain = str(urlparse(url).netloc)
            list_url.append(domain)
            if domain in sr_dofm:
                pass
            else:
                sr_dofm[domain] = date

    sr_url = pd.Series( sr_dofm.keys() )
    sr_value_count = sr_url.value_counts(ascending=True)

    df_avg_day['dofm'] = sr_dofm
    df_avg_day['total'] = sr_value_count
    sr_url = pd.Series(list_url)
    sr_value_count = sr_url.value_counts(ascending=True)

    df_avg_day['dofm'] = sr_dofm
    df_avg_day['total'] = sr_value_count

    df_avg_day['day_avg'] = df_avg_day['total'].div(df_avg_day['dofm'].rsub(last_date).dt.days+1)
    df_avg_day = df_avg_day.sort_values(by='day_avg')
    pass
