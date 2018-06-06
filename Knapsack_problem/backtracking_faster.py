#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:11:37 2018

@author: i
"""
import numpy as np

def back(tab_w_v, d):
    sequence = np.zeros(len(tab_w_v))
    return backtracking(tab_w_v, d, 
                        sequence,
                        index=0, weight=0, current_profit=0)

def backtracking(tab_w_v, d,
                 sequence,
                 index=0, weight=0, current_profit=0):
    if weight > d:
        return -tab_w_v[index-1][1]
    if index > len(tab_w_v) - 1:
        return 0
    else:
        sequence_copy = sequence.copy()
        sequence_copy[index] = 1
        return max(backtracking(tab_w_v, d,
                                sequence_copy,
                                index + 1,
                                weight + tab_w_v[index][0],
                                current_profit + tab_w_v[index][1])
                   + tab_w_v[index][1],
                   backtracking(tab_w_v, d,
                                sequence,
                                index + 1, 
                                weight,
                                current_profit))