#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:40:47 2018

@author: i
"""        

#There is a lot of turn+=1 stuff.I give you pure code without it on the of the document. 
#I think that it will be easier to understand.

def DFS(Alist):
    explored = []
    turn = 1
    startAndEnd = {}
    for apodosisIndex ,apodosis in enumerate(Alist[1:], 1): # go through main vertixes set. We start from Alist[1:] because there is empty cell Alist[0]
        if apodosisIndex in explored: continue          # if vertex equal apodosisIndex was explored don.t go there
        explored.append(apodosisIndex)                  #append visited vertex
        startAndEnd[apodosisIndex] = [turn, 0]
        turn += 1
        for vertex in apodosis:
            if vertex in explored: continue             # if vertex was explored don't go there
            explored.append(vertex)                     #append visited vertex
            startAndEnd[vertex] = [turn, 0]
            turn += 1
            _DFS(vertex, Alist, explored, turn, startAndEnd)         #go to freshly visited vertex
            
            startAndEnd[vertex][1] = turn
            turn += 1
        startAndEnd[apodosisIndex][1] = turn
        turn += 1
    print(explored)                                     #at the end give me sequence list
    print(startAndEnd)
    
def _DFS(indexOfMainTable, Alist, explored, turn, startAndEnd):
    for vertex in Alist[indexOfMainTable]:              #go through visited neighbours
            if vertex in explored: continue             # if vertex was explored don't go there
            startAndEnd[vertex] = [turn, 0]
            turn += 1
            explored.append(vertex)                     
            _DFS(vertex, Alist, explored, turn, startAndEnd)                                #go to freshly visited vertex
            turn += 1
            startAndEnd[vertex][1] = turn
            turn += 1
            
            


def DFS2(Alist):
    explored = []
    for apodosisIndex ,apodosis in enumerate(Alist[1:], 1): # go through main vertixes set
        if apodosisIndex in explored: continue          # if vertex equal apodosisIndex was explored don.t go there
        explored.append(apodosisIndex)                  #append visited vertex
        for vertex in apodosis:
            if vertex in explored: continue             # if vertex was explored don't go there
            explored.append(vertex)                     #append visited vertex
            _DFS(vertex, Alist, explored)               #go to freshly visited vertex
    print(explored)                                     #at the end give me sequence list
    
def _DFS2(indexOfMainTable, Alist, explored, turn, startAndEnd):
    for vertex in Alist[indexOfMainTable]:              #go through visited neighbours
            if vertex in explored: continue             # if vertex was explored don't go there
            explored.append(vertex)                     
            _DFS(vertex, Alist, explored)              #go to freshly visited vertex

            
            
            
            
            
            
            
            