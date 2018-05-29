#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:42:44 2018

@author: i
"""
import matplotlib.pyplot as plt
import pandas as pd

def myPlot(x, data, legend = '', columnNames = '', xlabel = '', ylabel = '', title = ''):
    #Plot
    for y in data:
        plt.plot(x, y, 'o-')
    plt.legend(legend, loc='upper left')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
    #Show tables
    d = {}
    for name, y in zip(columnNames, data):
        d[name] = y
    print(pd.DataFrame(data=d, index=x))
   # d = {'SS':ySS, 'IS':yIS, 'BS':yBS, 'HS':yHS, 'MS':yMS, 'CS':yCS, 'QSside':yQSside, 'QSmiddle':yQSmiddle}
    
