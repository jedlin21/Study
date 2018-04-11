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

#Prepare hight tables:
hTR = []
hTB = []

for multiplier in range(1,11):
    tabRandom = np.array
    tabRandom = np.random.randint(1000000*multiplier, size=10*multiplier) #make table multiplier * 1,000 where multiplier[1,10]
    
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
        
        









###############################################################################
            #Plot data
###############################################################################


### 1
#cB cL cTR cTB (x)
legend = ["cB", "cL", "cTR"]   # , "cTB"
data = [cB, cL, cTR]           # , cTB
myPlot(X, data, legend)


### 2 
legend = ["sB", "sbB", "sL", "sTR"]      ### Tu brakuje jeszcze sTB!!!!!!!!!!!!!!!!
data = [sB, sbB, sL, sTR]
myPlot(X, data, legend)


### 3
legend = ["hTR"]      # , "hTB"
data = [hTR]          # , hTB                          
myPlot(X, data, legend)













       
        
        
        

        
        
        
        
        
        
        
        