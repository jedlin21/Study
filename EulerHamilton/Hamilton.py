#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:40:47 2018

@author: Patryk Jedlikowski

Find one Hamilton path or all Hamilton paths by DFS algorithm 
"""


def DFS_Hamilton_one(AL):
    """Go throw AL list. When there is connection between vertex and next 
    vertex go there. 
    If there is no Hamilton path return False"""
    global flag
    global H_sequence
    flag = False
    explored = [0]
    for vertex in AL[0]: 
        _DFS_Hamilton_one(explored, AL, 0, vertex)  
        if flag:
            return H_sequence
    return False                              
    
def _DFS_Hamilton_one(explored, AL, previous, nextV):
    """Append nextV to explored list. If you have visited all vertices 
    and first vertex is equal to last vertex we find Hamilton path.
    Set flag to True and append explored to H_sequence"""
    global flag
    if flag: 
            return
    global H_sequence
    explored.append(nextV)
    if len(explored) == len(AL):
            flag = True
            H_sequence = explored[:]
    for vertex in AL[nextV]:
        if flag: 
            return
        if vertex in explored:
            continue
        _DFS_Hamilton_one(explored, AL, nextV, vertex) 
        
        if flag: 
            return
    explored.pop() 
   


def DFS_Hamilton_all(AL):
    """Go throw AL list. When there is connection between vertex and next 
    vertex go there. 
    Return all founded Hamilton paths."""
    global H_sequences
    H_sequences = []
    explored = [0]
    for vertex in AL[0]: 
        _DFS_Hamilton_all(explored, AL, 0, vertex)  
    return H_sequences
                             
    
def _DFS_Hamilton_all(explored, AL, previous, nextV):
    global H_sequences
    """Append nextV to explored list. 
    If you have visited all vertices 
    and first vertex is equal to last vertex we find Hamilton path.
    Sppend explored to H_sequences
    If len(explored) is smaller than vertices amount look futher.
    When you come back from _DFS_Hamilton_all pop last vertex 
    from explored list"""
    explored.append(nextV)
    if (len(explored) == len(AL) 
        and explored[0] in AL[nextV]):   #And there is connection beetwen 
        H_sequences.append(explored[:])            #first and last vertex
    for vertex in AL[nextV]:
        if vertex in explored:
            continue
        _DFS_Hamilton_all(explored, AL, nextV, vertex)
    explored.pop()             #clear last  vertex when exit recursion step
        