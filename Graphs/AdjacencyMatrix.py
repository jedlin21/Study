#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:56:34 2018

@author: i
"""

#create adjacency matrix

import numpy as np
import numpy.ma as ma

def makeAM(vertex, howManyOnes):       #how many vertex there are in the graph,  % of connections 
    adjacencyM = np.random.rand(vertex, vertex)                  # make random matrix
    zeros = ma.masked_greater(adjacencyM, howManyOnes).mask       #find where elements are greater than X
    ones = ma.masked_less_equal(adjacencyM, howManyOnes).mask     #find where elements are less than X
    
    adjacencyM[zeros] = 0                     # mask = 0
    adjacencyM[ones] = 1                      # mask = 1
    
    return adjacencyM