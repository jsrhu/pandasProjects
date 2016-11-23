#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////

dataHandler.py
Created on Tue Oct 25 09:52 2016
@author: jsrhu

CLASS FILE

////////////////////////////////////////////////
------------------------------------
Packages
------------------------
STDLIB:
datetime

MAINTAINED:
pandas
tqdm

CUSTOM:
lib.readWriteData

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
Classes
------------------------
dataFilter
------------
histFilter
liveFilter

------------------------
storage
------------

------------------------
analyzer
------------

------------------------------------
Functions
------------------------
Public
------------

------------------------
Private
------------

////////////////////////////////////////////

TODO:
Implement data connection

////////////////////////////////////////////////
"""
import pandas as pd
import datetime as dt
from tqdm import tqdm

import lib.readWriteData as rwd

class dataFilter(object):
    """
    Base Class for data filters. Historical Filter for Backtest sub-system and Live Filter for Live Trading sub-system
    """
    def __init__(self, filter_lifespan = 1, filter_update_period = 1, hist_data_sources = [], live_data_sources = [], **kwds):
        """
        Constructor for dataFilter class

        Parameters:
        self -
        filter_lifespan -
        filter_update_period -
        hist_data_sources -
        live_data_sources -

        Return:
        None
        """

        self._lifespan = dt.timedelta(days=filter_lifespan)
        self._update_period = dt.timedelta(days=filter_update_period)
        self._hist_data_sources = hist_data_sources
        self._live_data_sources = live_data_sources

    @property
    def lifespan(self):
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value):
        if value < 1:
            raise ValueError("Filter Lifespan must be at least 1 day long, i.e. Lifespan must be non-zero and positive")
        if not isinstance(value,(int,long)):
            raise TypeError("Filter Lifespan must be set in whole days, i.e. Lifespan value must be an integer")
        self._lifespan = dt.timedelta(days=value)

    @property
    def update_period(self):
        return self._update_period

    @update_period.setter
    def update_period(self, value):
        if value < 1:
            raise ValueError("Filter Update Period must be at least 1 day long, i.e. Update Period must be non-zero and positive")
        if not isinstance(value,(int,long)):
            raise TypeError("Filter Update Period must be set in whole days, i.e. Update Period value must be an integer")
        self._update_period = dt.timedelta(days=value)

    @property
    def hist_data_sources(self):
        return self._hist_data_sources

    @hist_data_sources.setter
    def hist_data_sources(self, sources):
        #raise error on object types in list?
        if sources == None:
            raise ValueError("Source list cannot be empty")
        self._hist_data_sources = sources

    @property
    def live_data_sources(self):
        return self._live_data_sources

    @live_data_sources.setter
    def live_data_sources(self, sources):
            #raise error on object types in list?
        if sources == None:
            raise ValueError("Source list cannot be empty")
        self._live_data_sources = sources

    def rawFilter(self, data = pd.DataFrame(), columns = [], black = False):
        """
        Filter raw data to create a pandas DataFrame

        Parameters:
        data -
        columns -
        black -

        Return:
        function - returns pandas DataFrame
        """
        if black == True:
            return self._rawBlacklist(data, columns)
        else:
            return self._rawWhitelist(data, columns)

    def _rawBlacklist(self, data, columns = []):
        """
        Private function for filter class that returns a subsection of a pandas DataFrame using a blacklist of DataFrame columns.

        Parameters:
        columns -

        Return:
        df - pandas DataFrame
        """
        df = rwd.readToDF(data)
        filtered = df.drop(columns, axis = 1)
        return filtered

    def _rawWhitelist(self, data, columns = []):
        """
        Private function for filter class that returns a subsection of a pandas DataFrame using a whitelist of DataFrame columns.

        Parameters:
        columns -

        Return:
        df - pandas DataFrame
        """
        df = rwd.readToDF(data)
        filtered = df[columns]
        return filtered

    def calcFilter(self, data = pd.DataFrame(), columns = [], functions = [], black = False):
        """
        Filter raw data through the use of a calculated function from the data properties

        Parameters:
        data -
        columns -
        functions -
        black -

        Return:
        function - returns pandas DataFrame
        """
        if black == True:
            return self._calcBlacklist(data, columns, functions)
        else:
            return self._calcWhitelist(data, columns, functions)

    def _calcBlacklist(self, data, columns, functions):
        """
        Private function for filter class that returns a subsection of a pandas DataFrame using functions to create a blacklist of DataFrame columns.

        Parameters:
        data -
        columns -
        functions -

        Return:
        df - pandas DataFrame
        """
        df = data
        for function in functions:
            df = function(data,inplace=True)
        return df

    def _calcWhitelist(self, data, columns, functions):
        """
        Private function for filter class that returns a subsection of a pandas DataFrame using functions to create a blacklist of DataFrame columns.

        Parameters:
        data -
        columns -
        functions -

        Return:
        df - pandas DataFrame
        """
        df = data
        for function in functions:
            df = function(data,inplace=True)
        return df

class histFilter(dataFilter):
    """
    Historical Filter for Backtest sub-system
    """
    def __init__(self, filter_lifespan = 1, filter_update_period = 1, **kwds):
        """
        Constructor for histFilter class

        Parameters:
        self -
        filter_lifespan -
        filter_update_period -

        Return:
        None
        """
        base = dataFilter(filter_lifespan = filter_lifespan, filter_update_period = filter_update_period, hist_data_sources = [])
        self._lifespan = base.lifespan
        self._update_period = base.update_period
        self._hist_data_sources = base.hist_data_sources

class liveFilter(dataFilter):
    """
    Live Filter for Live trading sub-system
    """
    def __init__(self, filter_lifespan = 1, filter_update_period = 1, **kwds):
        """
        Constructor for liveFilter class

        Parameters:
        self -
        filter_lifespan -
        filter_update_period -

        Return:
        None
        """
        base = dataFilter(filter_lifespan = filter_lifespan, filter_update_period = filter_update_period, live_data_sources = [])
        self._lifespan = base.lifespan
        self._update_period = base.update_period
        self._live_data_sources = base.live_data_sources

    def connect(self, source):
        """
        Connect to a given data source.

        Parameters:
        source

        Return:
        connection
        """
        connection = source
        return connection

    def readConnection(self, connection):
        """
        Read information form a connection to a data source.

        Parameters:
        connection

        Return:
        data
        """
        data = connection
        return data

    def update(self):
        """
        Parameters:
        self

        Return:
        event - event object
        """
        return event

class storage(object):
    """
    Storage for unanalyzed data.
    """
    def __init__(self):
        """
        Constructor for storage.

        Parameters:
        self

        Return:
        None
        """
        pass

class analyzer(object):
    """
    Analyzer for unanalyzed data.

    """
    def __init__(self):
        """
        Constructor for analyzer.

        Parameters:
        self

        Return:
        None
        """
        pass
