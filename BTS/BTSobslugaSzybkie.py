#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:57 2018

@author: i
"""
from BTS import Tree
from Bisection import Bisection
from Plot import myPlot
import numpy as np
import time
import sys
sys.setrecursionlimit(12500)


#Prepare count table
X = []

#Prepare time tables:
### 2 ###
cB = []
sB = []
sbB = []
### 3 ###
cL = []
sL = []
### 4 ###
cTR = []
sTR = []
### 5 $$$
cTB = []
sTB = []
csortTB = []
### 6 ###
pListSearch = []
pListCreation = []


#Prepare hight tables:
hTR = []
hTB = []

for multiplier in range(1,4):
    tabRandom = np.array
    tabRandom = np.random.randint(1000000000*multiplier, size=1000000*multiplier) #make table multiplier * 1,000 where multiplier[1,10]
    
    X.append(tabRandom.size)  
########################### 2 #################################################
    start = time.time()
    tabCopy = np.array                  #copying          
    tabCopy = np.copy(tabRandom)     
    tabCopy.sort(kind='quicksort')       #Sort tabCopy  
    end = time.time()
    cB.append(end - start)         

    start = time.time()
    for val in tabRandom:            #find values in the unsorted tabCopy by bisection search
        Bisection(val, tabCopy)
    end = time.time()
    sbB.append(end - start)
    
############################ 3 ################################################





    
################################## 4 ##########################################
    start = time.time()
    tree = Tree()               #BTS creation
    for elem in tabRandom:
        tree.add(elem)
    end = time.time()
    cTR.append(end - start)
    
    hTR.append(tree.height())      #height
    
    start = time.time()         ###Searching
    for elem in tabRandom:
        tree.find(elem)
    end = time.time()
    sTR.append(end - start)
#################################### 5 ########################################        
    start = time.time()         
    tabHelper = []
    tabHelper = tabRandom
    tabHelper.sort(kind='quicksort')
    tabSortTB = []
    left = 0
    right = len(tabHelper)
    def SortTB(tab, left, right):
        if left != right:
            middle = (left+right)//2
            x = tabHelper[middle]
            tabSortTB.append(x)      #przygotowanie tablicy dla drzewa TB przez dzielenie połówkowe
            SortTB(tab, left, middle)
            SortTB(tab, middle+1, right)
        return tabSortTB
    SortTB(tabSortTB, left, right)
    end = time.time()               # zmierz czas dla tworzenia tablicy wejściowej dla drzewa TB
    csortTB.append(end - start)

    start = time.time()
    tree = Tree()
    for elem in tabSortTB:              #BTS TB creation
        tree.add(elem)
    end = time.time()
    cTB.append(end - start)

    hTB.append(tree.height())               #height

    start = time.time()                     #Searching
    for elem in tabSortTB:
        tree.find(elem)
    end = time.time()
    sTB.append(end - start)


#################################### 6 ######################################## 
#Python
    start = time.time()
    pList = []
#    for elem in tabRandom:
#        pList.append(elem)
    end = time.time()
    pListCreation.append(end - start)
    
    start = time.time()
#    for elem in tabRandom:      ###Searching
#        elem in pList         
    end = time.time()
    pListSearch.append(end - start)
    
    
    print("Done ", multiplier, "/10")

        









###############################################################################
                                #Plot data
###############################################################################


### 1
#cB cL cTR cTB (x)
legend = ["Kopiowanie i sortowanie tablicy", "Budowa drzewa BST", "Budowa drzewa zrównoważonego", "Tworzenie listy wbudowanej w Python"]  
columnNames = ["cB", "cTR", "cTB", "Lista Python"]  
data = [cB, cTR, cTB, pListCreation]
myPlot(X, data, legend, columnNames,"Ilość elementów", "Czas [s]", "Zależność czasu tworzenia struktur od liczby elementów")


### 2 
#legend = ["Bisection search","Szukanie w drzewie BST", "Szukanie w drzewie zrównoważonym TB", "Szukanie liście wbudowanej Python"]      ### Tu brakuje jeszcze sTB!!!!!!!!!!!!!!!!
#columnNames = ["sbB", "sTR", "sTB", "S Lista Python"]
#data = [sbB, sTR, sTB, pListSearch]
#myPlot(X, data, legend, columnNames, "Ilość elementów", "Czas [s]", "Zależność czasu wyszukiwania od liczby elementów")

### 2 
legend = ["Bisection search","Szukanie w drzewie BST", "Szukanie w drzewie zrównoważonym TB"]      ### Tu brakuje jeszcze sTB!!!!!!!!!!!!!!!!
columnNames = ["sbB", "sTR", "sTB"]
data = [sbB, sTR, sTB]
myPlot(X, data, legend, columnNames, "Ilość elementów", "Czas [s]", "Zależność czasu wyszukiwania od liczby elementów")


legend = ["Bisection search","Szukanie w drzewie BST", "Szukanie w drzewie zrównoważonym TB"]      ### Tu brakuje jeszcze sTB!!!!!!!!!!!!!!!!
columnNames = ["sbB", "sTR", "sTB"]
data = [np.add(sbB, cB), np.add(sTR, cTR),np.add(np.add(sTB, cTB), csortTB)]
myPlot(X, data, legend, columnNames, "Ilość elementów", "Czas [s]", "Zależność czasu wyszukiwania od liczby elementów gdy bierzemy pod uwagę także czas tworzenia struktury")

### 3
legend = ["Wysokość drzewa TR", "Wysokość drzewa zrównoważonego TB"]
columnNames = ["hTR", "hTB"]
data = [hTR, hTB]                      
myPlot(X, data, legend, columnNames, "Ilość elementów", "Wysokość drzewa", "Zależność wysokości drzewa od liczby elementów")


















