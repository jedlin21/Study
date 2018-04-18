#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:11:45 2018

@author: i
"""

def makeAdjacencyList(adjacencyMatrix):
    adjacencyList = [[]]                # create empty adjacencyList where size will be vertex amount + 1. We don't use 0 index 
    for rowIndex, row in enumerate(adjacencyMatrix, 1):
        adjacencyList.append([])                      #add vertex
        
        for elemIndex, elem in enumerate(row, 1):
            if(elem):                                   #if there is connection(elem == 1) with elemIndex element then add this value to connection set
                adjacencyList[rowIndex].append(elemIndex)      #make connection
    return adjacencyList