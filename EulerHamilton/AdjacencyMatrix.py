#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:56:34 2018

@author: i
"""

#create adjacency matrix

import numpy as np

def makeEulerAM(verticies, destiny):
    """The algoryth create euler matrix
    First we make empty matrix verticies x verticies
    and our start vertex"""
    eulerAM = np.zeros((verticies, verticies))
    startingVertex = vertexToConnect = 0
    previousVertex = np.random.randint(verticies)
    for counter in range(int((destiny * verticies * verticies)/2 - 1)):
        """When you draw by lot verticies where there is a connecton, draw lots 
        again
        When everything is ok, make 1 in the eulerAM and change previousVertex
        to vertexToConnect
        Then check for empty verticies and connect them
        At the end connect closing vertex to starting vertex"""
        while (eulerAM[previousVertex][vertexToConnect] == 1 
               or previousVertex == vertexToConnect):
            if sum(eulerAM[previousVertex]) == len(eulerAM)-1:#-1 because loops
                previousVertex = vertexToConnect
                vertexToConnect = np.random.randint(verticies)
            vertexToConnect = np.random.randint(verticies)
        makeConnection(previousVertex, vertexToConnect, eulerAM)
        previousVertex = vertexToConnect
        vertexToConnect = np.random.randint(verticies)
    noConnected = checkForNoConnections(eulerAM)
    for vertex in noConnected:
        if previousVertex == vertex: continue
        makeConnection(previousVertex, vertex, eulerAM)
        previousVertex  = vertex
    noConnected = checkForOneConnections(eulerAM)
    for vertex in noConnected:
        if previousVertex == vertex: continue
        makeConnection(previousVertex, vertex, eulerAM)
        previousVertex  = vertex
    if previousVertex != startingVertex:
        makeConnection(previousVertex, startingVertex, eulerAM)
    return eulerAM

def makeConnection(firstVertex, secondVertex, AM):
    AM[firstVertex][secondVertex] = 1
    AM[secondVertex][firstVertex] = 1
    
def checkForNoConnections(AM):
    #Check for no connected verticies and when you find one add it to 
    #noConnected list. Retur noConnected list.
    noConnected = []
    for rowIndex, row in enumerate(AM):
        if row.sum() < 1:     
            noConnected.append(rowIndex)
    return noConnected

def checkForOneConnections(AM):
    #Check for no connected verticies and when you find one add it to 
    #noConnected list. Retur noConnected list.
    noConnected = []
    for rowIndex, row in enumerate(AM):
        if row.sum() < 2:     
            noConnected.append(rowIndex)
    return noConnected

def deleteConnection(firstVertex, secondVertex, AM):
    AM[firstVertex][secondVertex] = 0
    AM[secondVertex][firstVertex] = 0
    
def deleteLoops(AM):
    for index in range(AM[0].size):
        if AM[index][index]:
           AM[index][index] = 0 
    