#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:57 2018

@author: i
"""
from AdjacencyMatrix import makeAM
from AdjacencyList import makeAdjacencyList
from EdgesTable import makeEdgeTable
from DFS import DFS
from returnEdges import returnEdgesAM, returnEdgesAL, returnEdgesET
from Plot import myPlot
import time
import sys
sys.setrecursionlimit(12500)

#data to change
n = 10


#Prepare count table
X = []

#Prepare time tables:
### 2 ###
timeObliczanieEtykietd02 = []
timeObliczanieEtykietd04 = []

### 3 ###
returnEdgesCounterd02 = []
returnEdgesCounterd04 = []

### 4 $$$
timeReturnEdgesAM02 = []
timeReturnEdgesAL02 = []
timeReturnEdgesET02 = []
timeReturnEdgesAM04 = []
timeReturnEdgesAL04 = []
timeReturnEdgesET04 = []




for multiplier in range(1,11):
    
    am02 = makeAM(multiplier * n, 0.2)          #AdjacencyMatrix with destiny 20%
    am04 = makeAM(multiplier * n, 0.4)          #AdjacencyMatrix with destiny 40%
    al02 = makeAdjacencyList(am02)              #Adjacency list with destiny 20%
    al04 = makeAdjacencyList(am04)              #Adjacency list with destiny 40%
    et02 = makeEdgeTable(am02)                  #edges table with destiny 20%
    et04 = makeEdgeTable(am04)                  #edges table with destiny 40%
    
    
    X.append(multiplier * n)  
########################### 2 #################################################
    #Przedstawić w tabeli i na wykresie (2 krzywe dla różnych wartości d) zależność czasu trwania etapu
    #obliczenia etykiet od liczby wierzchołków n.
    
    
    start = time.time()          
    _,_,entryExitTable02 = DFS(al02)    
    end = time.time()
    timeObliczanieEtykietd02.append(end - start) 

    start = time.time()          
    _,_,entryExitTable04 = DFS(al04)    
    end = time.time()
    timeObliczanieEtykietd04.append(end - start)         
    
############################ 3 ################################################
#Przedstawić w tabeli liczbę łuków powrotnych dla poszczególnych wartości liczby 
#wierzchołków n i gęstości d
    
    
    
    returnEdgesCounterd02.append(returnEdgesAL(al02, entryExitTable02))
    returnEdgesCounterd04.append(returnEdgesAL(al04, entryExitTable04))
    
    
    
    

    
################################## 4 ##########################################
#Przedstawić w 2 tabelach i na 2 wykresach dla różnych wartości d (3 krzywe dla różnych reprezentacji
#grafu na każdym wykresie) zależność czasu trwania etapu zliczania liczby łuków powrotnych od liczby
#wierzchołków n.
    
    

    #return edges for adjacency matrix of 20% destiny
    start = time.time()
    print(returnEdgesAM(am02, entryExitTable02))
    end = time.time()
    timeReturnEdgesAM02.append(end - start)
    
    #return edges for adjacency list of 20% destiny
    start = time.time()
    print(returnEdgesAL(al02, entryExitTable02))
    end = time.time()
    timeReturnEdgesAL02.append(end - start)
    
    #return edges for edges table of 20% destiny
    start = time.time()
    print(returnEdgesET(et02, entryExitTable02))
    end = time.time()
    timeReturnEdgesET02.append(end - start)
    
    
    #return edges for adjacency matrix of 40% destiny
    start = time.time()
    print(returnEdgesAM(am04, entryExitTable04))
    end = time.time()
    timeReturnEdgesAM04.append(end - start)
    
    #return edges for adjacency list of 40% destiny
    start = time.time()
    print(returnEdgesAL(al04, entryExitTable04))
    end = time.time()
    timeReturnEdgesAL04.append(end - start)
    
    #return edges for edges table of 40% destiny
    start = time.time()
    print(returnEdgesET(et04, entryExitTable04))
    end = time.time()
    timeReturnEdgesET04.append(end - start)
    




    
    
    print("Done ", multiplier, "/10")





###############################################################################
                                #Plot data
###############################################################################

### 1

legend = ["Gęstość 20%", "Gęstość 40%"]  
columnNames = ["Gęstość 20%", "Gęstość 40%"]  
data = [timeObliczanieEtykietd02, timeObliczanieEtykietd04]
myPlot(X, data, legend, columnNames,"Ilość wierzchołków", "Czas [s]", "Zależność czasu trwania etapu tworzenia etykiet od gęstości grafu")


### 2 
legend = ["Gęstość 20%", "Gęstość 40%"]
columnNames = ["Gęstość 20%", "Gęstość 40%"]
data = [returnEdgesCounterd02, returnEdgesCounterd04]
myPlot(X, data, legend, columnNames, "Ilość wierzchołków", "Ilość krawędzi powrotnych", "Zależność ilości krawędzi powrotnych od ilości wierzchołków")


### 4
legend = ["Macierz sąsiedztwa", "Lista następników", "Lista krawędzi"]
columnNames = ["Macierz sąsiedztwa", "Lista następników", "Lista krawędzi"]
data = [timeReturnEdgesAM02, timeReturnEdgesAL02, timeReturnEdgesET02]                      
myPlot(X, data, legend, columnNames, "Ilość wierzchołków", "Czas [s]", "Czas zliczania liczby łuków powrotnych dla różnych reprezentacji grafu. Zagęszczenie grafu 20%")

legend = ["Macierz sąsiedztwa", "Lista następników", "Lista krawędzi"]
columnNames = ["Macierz sąsiedztwa", "Lista następników", "Lista krawędzi"]
data = [timeReturnEdgesAM04, timeReturnEdgesAL04, timeReturnEdgesET04]                      
myPlot(X, data, legend, columnNames, "Ilość wierzchołków", "Czas [s]", "Czas zliczania liczby łuków powrotnych dla różnych reprezentacji grafu. Zagęszczenie grafu 40%")





















