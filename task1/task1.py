import sys
import gzip

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

compressed_data_2014 = '../data/2014all_head.csv.gz'
compressed_data_2015 = '../data/2015all_head.csv.gz'
compressed_data_2016 = '../data/2016all_head.csv.gz'

dataframe_2014 = pd.read_csv(compressed_data_2014,chunksize=4)

for chunk in dataframe_2014:
    print chunk
