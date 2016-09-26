'''
Now that you have the data, the first task is to verify all their fields, e,g, if source_rank is claimed to be from [1,10], then this should be true every single day.
To do this, what you have to do is to plot the daily maxes and daily mins for source_rank for each day (see plot below for an example).
Note that python has a lot of vectorized operations.
If you find that you're doing a brute force iteration, i.e.

	for i in range( N ):
		do stuff on array[i]

then there may be a faster way.
Avoid brute force iteration if at all possible.

This verification can be done for any bounded numeric field.
And we should certainly verify all of them.

Secondly, we can also aggregate a list of URLs which they scrape.
I think it would be interested in compiling a catalog of unique URLs.
You would essentially extract the URL pandas series from the dataframe look at the source website (this will involve using split) and then keep unique values.

The same thing could be done for the list of tickers.
'''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

compressed_data_2014 = '../data/2014all_head.csv.gz'
compressed_data_2015 = '../data/2015all_head.csv.gz'
compressed_data_2016 = '../data/2016all_head.csv.gz'

dataframe_2014 = pd.read_csv(compressed_data_2014, nrows=1000, header=0)
dataframe_2015 = pd.read_csv(compressed_data_2015, nrows=1000, header=0)
dataframe_2016 = pd.read_csv(compressed_data_2016, nrows=1000, header=0)


for column in dataframe_2014.columns:
    try:
        print "Minimum value of ",column,":",dataframe_2014[column].min()
        print "Maximum value of ",column,":",dataframe_2014[column].max()
        print
    except:
        print column
        pass
