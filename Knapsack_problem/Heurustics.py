#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:46:07 2018

@author: i
"""
import numpy as np
from operator import itemgetter

def make_tab(weights,values):
    weights = weights[1:]
    values = values[1:]
    tab_w_v = []    
    for x,y in zip(weights,values):
        tab_w_v.append([x,y])
    return tab_w_v
 
    
def H_random(tab_w_v, d):
    length = len(tab_w_v)
    sum_weight = 0
    sequence = []
    while(sum_weight < d):
        index = np.random.randint(length)
        while index in sequence:
            index = np.random.randint(length)
        sequence.append(index)
        sum_weight += tab_w_v[index][0]
    if sum_weight > d:
        sequence.pop()
    return (sequence, profit(sequence, tab_w_v))

def profit(explored_sequence, tab_w_v):
    values_sum = 0
    for item in explored_sequence:
        values_sum += tab_w_v[item][1]
    return values_sum

def H_min_weight_sort(tab_w_v, d):
    sorted_tab_wv = sorted(tab_w_v, key=itemgetter(0))
    sum_weight = 0
    profits = []
    sequence = []
    for elem in sorted_tab_wv:
        if sum_weight > d:
            break
        sequence.append(elem)
        profits.append(elem[1])
        sum_weight += elem[0]
    """Ckeck if last element fit. If not pop it."""
    if sum_weight > d:
        sequence.pop()
        profits.pop()
    return (sequence, sum(profits))

def H_max_value_sort(tab_w_v, d):
    sorted_tab_wv = sorted(tab_w_v, key=itemgetter(1), reverse=True)
    sum_weight = 0
    profits = []
    sequence = []
    for elem in sorted_tab_wv:
        if sum_weight > d:
            break
        sequence.append(elem)
        profits.append(elem[1])
        sum_weight += elem[0]
    """Ckeck if last element fit. If not pop it."""
    if sum_weight > d:
        sequence.pop()
        profits.pop()
    return (sequence, sum(profits))

def H_quotient_values_and_weights(tab_w_v, d):
    sorted_tab_wv = sorted(tab_w_v, key=lambda x: x[1]/x[0], reverse=True)
    sum_weight = 0
    profits = []
    sequence = []
    for elem in sorted_tab_wv:
        if sum_weight > d:
            break
        sequence.append(elem)
        profits.append(elem[1])
        sum_weight += elem[0]
    """Ckeck if last element fit. If not pop it."""
    if sum_weight > d:
        sequence.pop()
        profits.pop()
    return (sequence, sum(profits))

















