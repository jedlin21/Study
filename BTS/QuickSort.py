#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:54:47 2018

@author: i
"""

# Quick sort(middle)
def QuickSort(tab, left=0, right=None):
    if right is None: right = len(tab) - 1
    i, j = left, right
    pivot = tab[(left + right) // 2]
    while i <= j:
        while tab[i] < pivot: i += 1
        while tab[j] > pivot: j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1; j -= 1
    if left < j: QuickSort(tab, left, j)
    if right > i: QuickSort(tab, i, right)