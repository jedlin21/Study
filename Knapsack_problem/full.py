#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:06:08 2018

@author: i
"""
import numpy as np

"""Find the best value and indexes of knapsack problem by look at all 
   the possibilities """
def full(n, d, weights, values):
    """Let's mask be like binary number. Multiply weights and mask and check if
    it is smaller than knapsack.
    If it is smaller then copare sum of values with max_value."""
    mask = np.zeros(n+1)
    max_value = 0
    for x in range(2**n):
        if (mask * weights).sum() <= d:
            bufor = mask * values
            bufor = bufor.sum()
            if bufor > max_value:
                max_value = bufor
                indexes = mask.copy()
        """Binary addition on the mask"""
        for i in range(1, len(mask)):
            if mask[-i]:
                mask[-i] = 0
            else:
                mask[-i] = 1
                break
    return (max_value, indexes)
            
        