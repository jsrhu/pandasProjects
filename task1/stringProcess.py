#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:48:04 2016

@author: jsrhu
"""

import string

def removePunctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s