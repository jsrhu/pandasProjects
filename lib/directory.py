#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
////////////////////////////////////////////////

lib.directory.py
Created on Thurs Nov 17 15:13 2016
@author: jsrhu

LIBRARY FILE

////////////////////////////////////////////////
------------------------------------
Packages
------------------------
STDLIB:
os

MAINTAINED:

CUSTOM:

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
checkPath
createDir
changeDir
moveFileToDir

------------------------
Private
------------

////////////////////////////////////////////

TODO:

////////////////////////////////////////////////
"""
import os

def checkPath(path,is_file=True):
    """
    Checks the existence of a given path

    Parameters:
    path - string representation of path to be checked

    Return:
    boolean - boolean result of check; False if the directory does not exist or cannot be read from or written to, True otherwise
    possibly return a string/key to indicate state
    """
    if is_file:
        if not os.path.isfile(path):
            print 'File not found: check the file path'
            return False
        else:
            return True

def createDir(path):
    """
    Attempts to create directory for plot images.

    Parameters:

    Return:
    path -
    """
    try:
        os.mkdir(path)
        return path
    except OSError:
        print "Directory path already exists"
        return path



    elif not is_file:
        if not os.path.isdir(path):
            print "Directory not found: check the filepath"
            return False
        else:
            return True

def changeDir(destination = None):
    if checkPath(path):  #not neccesarily neccesary
        os.chdir(destination)

def moveFileToDir(target_file = None, destination_file = None):
    if checkPath(target_file):
        os.rename(target_file,destination_file)
