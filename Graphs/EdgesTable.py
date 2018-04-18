#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:04:57 2018

@author: i
"""
import numpy as np

def makeEdgeTable(adjacencyMatrix):
     edgeTable = np.zeros((int(adjacencyMatrix.sum()), 2), dtype=np.int)    #prepare edges x 2 table
     edgeIndex = 0
     for rowIndex, row in enumerate(adjacencyMatrix, 1):        #iterate throught row in matrix
        for elemIndex, elem in enumerate(row, 1):               # iterate throught element in row
            if(elem):                                   #if there is connection(elem == 1) with elemIndex element then add this value to connection set
                edgeTable[edgeIndex][0], edgeTable[edgeIndex][1] = rowIndex, elemIndex  # make connection
                edgeIndex += 1
     return edgeTable
                