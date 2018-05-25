#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:27:03 2018

@author: i
"""
from weightAndValues import make_Weights_and_values

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
    