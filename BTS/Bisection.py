#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:00:53 2018

@author: i
"""
import numpy as np

#Jeśli szukany element występuje F=funkcja zwraca indeks szukanego elementu
#Jeśli element nie występuje funkcja zwraca False

def Bisection(val, tab):
    left = 0
    right = tab.size
    flag = 0
            #size even       size odd
    while(left != right and flag != 2):
        x = (left + right) // 2
        if(tab[x] == val):
            return True
        elif(tab[x] < val):
            left = x
        elif(tab[x] > val):
            right = x
        
        if(left + 1 == right):
            flag += 1
    return False