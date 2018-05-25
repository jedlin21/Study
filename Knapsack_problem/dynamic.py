#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:27:03 2018

@author: i
"""
#from weightAndValues import make_Weights_and_values



"""Find the best value of knapsack problem by dynamic programming """
def dynamic(i, l, weights, values):
    if l == 0:
        return 0
    elif i == 0:
        return 0
    else:
        if weights[i] > l:
            return dynamic(i-1, l, weights, values)
        else:
            return max(dynamic(i-1, l, weights, values),
                       dynamic(i-1, l-weights[i], weights, values) + values[i])
    
"""Check which indexes give the best value of knapsack problem 
    by dynamic programming """
def find_the_best_indexes(i, l, weights, values):
    tab_indexes = []  
    for x in range(i+1):
        tab_indexes.append(x)    
    _set_indexes(i, l, weights, values, tab_indexes)
    return tab_indexes
    
def _set_indexes(i, l, weights, values, tab_indexes):
    if i == 0:
        return 
    if dynamic(i, l, weights, values) == dynamic(i-1, l, weights, values):
        tab_indexes[i] = 0
        _set_indexes(i-1, l, weights, values, tab_indexes)
    else:
        tab_indexes[i] = 1
        _set_indexes(i-1, l-weights[i], weights, values, tab_indexes)
        
        
        
        
        
        
        
        
        