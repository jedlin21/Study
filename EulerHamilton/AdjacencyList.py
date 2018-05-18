#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:11:45 2018

@author: i
"""

def makeAdjacencyList(adjacencyMatrix):
    adjacencyList = [[]]                # create empty adjacencyList where size will be vertex amount
    for rowIndex, row in enumerate(adjacencyMatrix):
        adjacencyList.append([])                      #add vertex
        
        for elemIndex, elem in enumerate(row):
            if(elem):                                   #if there is connection(elem == 1) with elemIndex element then add this value to connection set
                adjacencyList[rowIndex].append(elemIndex)      #make connection
    adjacencyList.pop()
    return adjacencyList