#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:40:47 2018

@author: i
"""

from Bisection import Bisection

#Find Euleric path by DFS algorithm 
def DFS_Euler(AL):
    """Go throw AL list. When there is connection between vertex and next vertex
    go there. If there is no more fresh edge add vertex number to "explored" list.
    Returned "explored" list is Euleric path"""
    global explored
    global Alist
    Alist = AL[:]
    explored = []
    for index, vertex in enumerate(AL[0]):
        _DFS_Euler(vertex, index, 0)  
        explored.append(vertex)
    explored.append(0)
    Alist = ["hello"]
    return explored                                     
    
def _DFS_Euler(vIndex, index, rIndex):
    global explored
    global Alist
    """Delete connecton between rowIndex and Alist[rowIndex]
    First we destroy connection between rowIndex -> vertex
    Next we seek for index of vertex -> rowIndex connection in Alist[rowIndex]
    using bisection search
    Finally we delete connection between vertex -> rowIndex"""
    Alist[rIndex].pop(index)
    indexToDelete = Bisection(rIndex, Alist[vIndex])
    Alist[vIndex].pop(indexToDelete)
    for ind, vertex in enumerate(Alist[vIndex]):             
        _DFS_Euler(vertex, ind, vIndex)              
        explored.append(vertex)
