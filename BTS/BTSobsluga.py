#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:57 2018

@author: i
"""
from BTS import Tree
from MyList import MyList
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
### 6 ###
pListSearch = []
pListCreation = []

#Prepare hight tables:
hTR = []
hTB = []


for multiplier in range(1,21):
    tabRandom = np.array
    tabRandom = np.random.randint(1000000*multiplier, size=100*multiplier) #make table multiplier * 1,000 where multiplier[1,10]
    
    X.append(tabRandom.size)  
########################### 2 #################################################
    start = time.time()
    tabCopy = np.array                  #copying          
    tabCopy = np.copy(tabRandom)     
    tabCopy.sort(kind='quicksort')       #Sort tabCopy  
    end = time.time()
    cB.append(end - start)         

    start = time.time()                       
    for val in tabRandom:           #serching
        for x in tabCopy:           #find values in the unsorted tabCopy
            if(val == x):
                break
    end = time.time()
    sB.append(end - start)

    start = time.time()
    for val in tabRandom:            #find values in the unsorted tabCopy by bisection search
        Bisection(val, tabCopy)
    end = time.time()
    sbB.append(end - start)
    
############################ 3 ################################################
    start = time.time()
    myList = MyList()            ###List creation
    for elem in tabRandom:
        myList.add(elem)
    end = time.time()
    cL.append(end - start)
    
    
    start = time.time()
    for elem in tabRandom:      ###Searching
        myList.has(elem)        #If it has an element myList.has(elem) will return True 
    end = time.time()
    sL.append(end - start)
    
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
    for elem in tabRandom:
        pList.append(elem)
    end = time.time()
    pListCreation.append(end - start)
    
    start = time.time()
    for elem in tabRandom:      ###Searching
        elem in pList         
    end = time.time()
    pListSearch.append(end - start)
    
    
    print("Done ", multiplier, "/20")



###############################################################################
                                #Plot data
###############################################################################

### 1
#cB cL cTR cTB (x)
legend = ["Kopiowanie i sortowanie tablicy", "Budowa listy jednokierunkowej", "Budowa drzewa BST", "Budowa drzewa zrównoważonego", "Tworzenie listy wbudowanej w Python"]  
columnNames = ["cB", "cL", "cTR", "cTB", "Lista Python"]  
data = [cB, cL, cTR, cTB, pListCreation]
myPlot(X, data, legend, columnNames,"Ilość elementów", "Czas [s]", "Zależność czasu tworzenia struktur od liczby elementów")


### 2 
legend = ["Szukanie w tablicy", "Bisection search", "Szukanie w liście", "Szukanie w drzewie BST", "Szukanie w drzewie zrównoważonym TB", "Szukanie liście wbudowanej Python"]      ### Tu brakuje jeszcze sTB!!!!!!!!!!!!!!!!
columnNames = ["sB", "sbB", "sL", "sTR", "sTB", "S Lista Python"]
data = [sB, sbB, sL, sTR, sTB, pListSearch]
myPlot(X, data, legend, columnNames, "Ilość elementów", "Czas [s]", "Zależność czasu wyszukiwania od liczby elementów")


### 3
legend = ["Wysokość drzewa TR", "Wysokość drzewa zrównoważonego TB"]
columnNames = ["hTR", "hTB"]
data = [hTR, hTB]                      
myPlot(X, data, legend, columnNames, "Ilość elementów", "Wysokość drzewa", "Zależność wysokości drzewa od liczby elementów")





















