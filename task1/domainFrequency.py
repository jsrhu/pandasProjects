s# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:51:14 2016
@author: jsrhu
STATUS:
TODO
- change path to output to ignored directory
"""
import pandas as pd
import cPickle

import matplotlib.pyplot as plt

from urlparse import urlparse

def myurlparse(x):    
    try:
        return str(urlparse(x).netloc)
    except:
        return x    

'''
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
'''
df_avg_day = cPickle.load(open("../data/pickle/day_avg_data.p" ,"rb"))

print df_avg_day.head(50)
print df_avg_day.tail(50)
    
print df_avg_day['day_avg'].quantile([.1,.5,.99])
    
try:
    print 'Average daily reference to "www.benzinga.com":',df_avg_day['day_avg']['www.benzinga.com']
except:
    print 'The domain: "www.benzinga.com" could not be found.'
try:
    print 'Average daily reference to "www.bloomberg.com":',df_avg_day['day_avg']['www.bloomberg.com']
except:
    print 'The domain: "www.bloomberg.com" could not be found.'
try:
    print 'Average daily reference to "www.reuters.com":',df_avg_day['day_avg']['www.reuters.com']
except:
    print 'The domain: "www.reuters.com" could not be found.'
try:
    print 'Average daily reference to "finance.yahoo.com":',df_avg_day['day_avg']['finance.yahoo.com']
except:
    print 'The domain: "finance.yahoo.com" could not be found.'
try:
    print 'Average daily reference to "www.wsj.com":',df_avg_day['day_avg']['www.wsj.com']
except:
    print 'The domain: "www.wsj.com" could not be found.'

bin_range = [x for x in xrange(0, 50000, 1000)]
ax = df_avg_day['total'].plot.hist(logy=True, bins=bin_range, figsize=(11,8))
ax.set_ylabel('Number of Domains')
ax.set_xlabel('Number of Total References')
plt.tight_layout()
plt.savefig('domain_total.png')
plt.show()
plt.clf()

bin_range = [x for x in xrange(0,600,25)]
ax = df_avg_day['day_avg'].plot.hist(logy=True, bins=bin_range, figsize=(11,8))
ax.set_ylabel('Number of Domains')
ax.set_xlabel('Number of Average References')
plt.tight_layout()
plt.savefig('domain_day_avg.png')
plt.show()
plt.clf()