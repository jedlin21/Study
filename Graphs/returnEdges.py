#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:06:30 2018

@author: i
"""

#return how many there are return adges using start and end analizies list 

#Adjacency Matrix and startAndEnd list
def returnEdgesAM(AM, startAndEnd):
    howMany = 0
    for row in range(1, len(AM) + 1):
        for column in range(1, len(AM) + 1):
            if AM[row - 1][column - 1] == 0: continue               #if there is not connection continue
            if startAndEnd[column][0] < startAndEnd[row][0] and startAndEnd[row][0] < startAndEnd[row][1] and startAndEnd[row][1] < startAndEnd[column][1] :
                howMany += 1
            if row == column:      # if there is self connection
                howMany += 1
    return howMany
        
#Adjacency List and startAndEnd list
def returnEdgesAL(Alist, startAndEndList):
    howMany = 0
    for index, connections in enumerate(Alist[1:], 1):
        for vertex in connections:
            if startAndEndList[vertex][0] < startAndEndList[index][0] and startAndEndList[index][0] < startAndEndList[index][1] and startAndEndList[index][1] < startAndEndList[vertex][1] :
                howMany += 1
            if index == vertex:      # if there is self connection
                howMany += 1
    return howMany

#Edges Table and startAndEnd list
def returnEdgesET(ETable, startAndEndList):
    howMany = 0
    for connection in ETable:
        if startAndEndList[connection[1]][0] < startAndEndList[connection[0]][0] and startAndEndList[connection[0]][0] < startAndEndList[connection[0]][1] and startAndEndList[connection[0]][1] < startAndEndList[connection[1]][1] :
            howMany += 1
        if connection[0] == connection[1]:      # if there is self connection
            howMany += 1                     
    return howMany