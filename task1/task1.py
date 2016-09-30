# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:51:14 2016

@author: jsrhu

STATUS:
TODO
- add title slide to power point
- change path to output to ignored directory
"""
import os
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

from pptx import Presentation
from pptx.util import Inches

compressed_data = '../data/backtest_alpha_for_ernest.csv.gz'

headers = ['story_sentiment','story_volume','story_traffic','story_shares','article_sentiment','article_traffic','event_impact_score_overall','event_impact_score_entity_1','event_impact_score_entity_2','avg_day_sentiment']

plot_type = 'min_max'

layout_title = 0
layout_title_content = 1
layout_section_header = 2
layout_two_content = 3
layout_comparison = 4
layout_title_only = 5
layout_blank = 6
layout_content_caption = 7
layout_picture_caption = 8

'''
Reads gzip compressed csv file and converts date string into date-time object
Returns dataframerepresentation of csv file
'''
def readLimitedRows(csv_file, rows):
    date_format="%Y-%m-%d %H:%M:%S %Z"
    dateparse = lambda x: pd.datetime.strptime(x, date_format)
    return pd.read_csv(filepath_or_buffer=csv_file, compression='gzip', nrows=rows, header=0, date_parser=dateparse, parse_dates=["harvested_at"])

'''
Reads gzip compressed csv file and converts date string into date-time object
Does not return anything
'''
def readFull(csv_file):
    date_format="%Y-%m-%d %H:%M:%S %Z"
    dateparse = lambda x: pd.datetime.strptime(x, date_format)
    pd.read_csv(filepath_or_buffer=csv_file, compression='gzip', header=0, date_parser=dateparse, parse_dates=["harvested_at"])

'''
Returns dataframe with select columns from the original
'''
def selectColumnsDataFrame(data_frame,columns):
    data_frame = data_frame[columns]
    return data_frame

'''
TODO
'''
def increaseYScaleRange(plot,percentage):
    plot.ylim(df_min[column].min()-abs(.1*df_min[column].min()),df_max[column].max()+abs(.1*df_max[column].max()))

'''
Attempts to create directory for plot images
Returns path to directory
'''
def createDir(name, descriptor):
    path = name+'_'+descriptor
    try:
        os.mkdir(path)
        return path
    except:
        return path

def addImageSlide(presentation, layout, image_path):
    slide_layout = presentation.slide_layouts[layout]
    
    slide = presentation.slides.add_slide(slide_layout)
    
    left = Inches(1)
    top = Inches(1)
    height = Inches(5.5)
    return slide.shapes.add_picture(image_file=image_path, left=left, top=top, height=height)
    
def savePresentation(presentation, title):
    presentation.save(title+'.pptx')
    
df = readLimitedRows(csv_file=compressed_data,rows=10000)
df_max = pd.DataFrame()
df_min = pd.DataFrame()
    
df_group = df.groupby( df['harvested_at'].apply(lambda x: x.date() ) )

for key,group in df_group:
    group_max = group.max(numeric_only=True)
    group_min = group.min(numeric_only=True)
    group_max['date'] = key
    group_min['date'] = key
    
    df_max = pd.concat([df_max, group_max.to_frame().T])
    df_min = pd.concat([df_min, group_min.to_frame().T])
    
df_max.set_index(keys='date', inplace=True)
df_min.set_index(keys='date', inplace=True)
    
df_max = selectColumnsDataFrame(data_frame=df_max,columns=headers)
df_min = selectColumnsDataFrame(data_frame=df_min,columns=headers)
    
plot_dir = createDir(name=plot_type, descriptor='plots')
os.chdir(plot_dir)

presentation = Presentation()
descriptor = 'max_min_plot'
title_slide = presentation.slides.add_slide(presentation.slide_layouts[layout_title])
title_slide.shapes.title.text = 'Maximum and Minimum Plots of Quantitative Metrics in:\n'+'Accern Data'
    
for column in df_max:
    column_plot = df_max[column].plot()
    column_plot = df_min[column].plot(ax=column_plot, title=column, x_compat=True, rot=45, figsize=(11,8))
        
    plt.ylim(df_min[column].min()-abs(.1*df_min[column].min()),df_max[column].max()+abs(.1*df_max[column].max()))
    
    image_path = column+'_'+descriptor+'.png'
    plt.savefig(image_path)
    #plt.show()
    plt.clf()
    
    addImageSlide(presentation=presentation, layout=layout_blank, image_path=image_path)

os.chdir('..')
ppt_dir = createDir(name='ppt', descriptor=descriptor)
os.chdir(ppt_dir)
savePresentation(presentation,descriptor)