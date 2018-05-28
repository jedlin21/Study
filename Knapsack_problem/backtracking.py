#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:14:50 2018

@author: i
"""
import numpy as np

def backtracking(d, weights, values):
    """Go throw AL list. When there is not used connection between vertex and 
    next vertex go there. Calculate the weight. Compare it to max capacity. 
    If everything correct compare bufor_profit to maxprofit and make changes 
        if necessary.
    Else return to previous vertex."""
    weights = weights[1:]
    values = values[1:]
    global H_sequences
    H_sequences = []
    global max_profit
    max_profit = 0
    AL = make_AL(weights)
    explored = np.zeros(len(AL))
    explored_sequence = []
    for rowIndex, row in enumerate(AL): 
        for vertex in row: 
            _backtracking(explored_sequence, explored, AL, 
                          rowIndex, vertex, 
                          d, weights, values)  
    return (max_profit, H_sequences)
                             
def _backtracking(explored_sequence, explored, AL, 
                  previous, nextV, 
                  d, weights, values):
    """Append nextV to explored_sequence list. 
    If we do not fit pop changes and return.
    If you have visited all vertices 
    and first vertex is equal to last vertex we find Hamilton path.
    Sppend explored to H_sequences
    If len(explored) is smaller than vertices amount look futher.
    When you come back from _DFS_Hamilton_all pop last vertex 
    from explored list"""
    explored_sequence.append(nextV)
    if not it_will_fit(explored_sequence, weights, d):
        explored_sequence.pop()
        return
    global H_sequences
    global max_profit
    explored[nextV] = 1
    bufor_profit = profit(explored_sequence, values)
    if  bufor_profit > max_profit:   
        H_sequences = explored.copy()   
        max_profit = bufor_profit 
        print(max_profit, explored)
    for vertex in AL[nextV]:
        if explored[vertex]:
            continue
        _backtracking(explored_sequence, explored, AL, 
                      nextV, vertex, 
                      d, weights, values)
    explored[nextV] = 0            #clear last  vertex when exit recursion step
    explored_sequence.pop()

"""Check if it will fit"""
def it_will_fit(explored_sequence, weights, d):
    weight_sum = 0
    for item in explored_sequence:
        weight_sum += weights[item]
    if weight_sum <= d:
        return True
    else:
        return False

"""Calculate profit of exploated values"""
def profit(explored_sequence, values):
    values_sum = 0
    for item in explored_sequence:
        values_sum += values[item]
    return values_sum

"""make adjacency list (everything connecting with everything.)
Without loops"""
def make_AL(weights):
    A_list = []
    for x in range(len(weights)-1):
        A_list.append([])
        for y in range(len(weights)-1):
            if(x != y):
                A_list[x].append(y)
    return A_list