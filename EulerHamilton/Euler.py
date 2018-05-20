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
        print("I'm in the main loop", explored)
    explored.append(0)
    print(explored)                                     
    
def _DFS_Euler(vIndex, index, rIndex):
    global explored
    global Alist
    """Delete connecton between rowIndex and Alist[rowIndex]
    First we destroy connection between rowIndex -> vertex
    Next we seek for index of vertex -> rowIndex connection in Alist[rowIndex]
    using bisection search
    Finally we delete connection between vertex -> rowIndex"""
    print(Alist)
    print("rIndex", rIndex)
    print("index", index)
    print("vIndex", vIndex)
    Alist[rIndex].pop(index)
    indexToDelete = Bisection(rIndex, Alist[vIndex])
    Alist[vIndex].pop(indexToDelete)
    for ind, vertex in enumerate(Alist[vIndex]):             
        _DFS_Euler(vertex, ind, vIndex)              
        explored.append(vertex)
        print("I'm in the second loop", explored)

   


def lists_of_lists_has_only_empty_lists(List):
    for element in List:
        if len(element) != 0:
            return False
    return True









         
def transformDictionaryToList(dictionary):
    theList = [[]]
    for x in range(1, len(dictionary) + 1):
        theList.append(dictionary[x])
    return theList
        
            
                        
            
            
            
            
def DFS(Alist):
    explored = []
    global turn 
    turn = 1
    startAndEnd = {}
    for apodosisIndex ,apodosis in enumerate(Alist[1:], 1): # go through main vertixes set. We start from Alist[1:] because there is empty cell Alist[0]
        #print(apodosisIndex, apodosis)
        if apodosisIndex in explored: continue          # if vertex equal apodosisIndex was explored don.t go there
        explored.append(apodosisIndex)                  #append visited vertex
        startAndEnd[apodosisIndex] = [turn, 0]
        turn += 1
        for vertex in apodosis:
            if vertex in explored: continue             # if vertex was explored don't go there
            explored.append(vertex)                     #append visited vertex
            startAndEnd[vertex] = [turn, 0]
            turn += 1
            _DFS(vertex, Alist, explored, startAndEnd)         #go to freshly visited vertex
            
            startAndEnd[vertex][1] = turn
            turn += 1
        startAndEnd[apodosisIndex][1] = turn
        turn += 1
    return (explored, startAndEnd, transformDictionaryToList(startAndEnd))  #return explore sequence, startAndEnd dictionary and startAndEnd list
    
def _DFS(indexOfMainTable, Alist, explored, startAndEnd):
    global turn
    for vertex in Alist[indexOfMainTable]:              #go through visited neighbours
            if vertex in explored: continue             # if vertex was explored don't go there
            explored.append(vertex)
            startAndEnd[vertex] = [turn, 0]
            turn += 1
            _DFS(vertex, Alist, explored,startAndEnd)  #go to freshly visited vertex
            startAndEnd[vertex][1] = turn
            turn += 1
            
            
            
            
            
            
            