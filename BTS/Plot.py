#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:42:44 2018

@author: i
"""
import matplotlib.pyplot as plt
import pandas as pd

def myPlot(x, data, legend):
    #Plot
    for y in data:
        plt.plot(x, y)
    plt.legend(legend, loc='upper left')
    plt.show()
    
    #Show tables
    d = {}
    for name, y in zip(legend, data):
        d[name] = y
    print(pd.DataFrame(data=d, index=x))
   # d = {'SS':ySS, 'IS':yIS, 'BS':yBS, 'HS':yHS, 'MS':yMS, 'CS':yCS, 'QSside':yQSside, 'QSmiddle':yQSmiddle}
    
