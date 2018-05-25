#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:08:28 2018

@author: i
"""

import numpy as np


def make_Weights_and_values(how_many, max_w, max_v):
    weights = [0]
    values = [0]
    for x in range(how_many):
        weights.append(np.random.randint(1, max_w))
        values.append(np.random.randint(1, max_v))
    return (weights, values)