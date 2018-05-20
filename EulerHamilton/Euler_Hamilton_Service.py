#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:57 2018

@author: i
"""
from AdjacencyMatrix import makeEulerAM
from AdjacencyList import makeAdjacencyList
from Hamilton import DFS_Hamilton_one, DFS_Hamilton_all
from Euler import DFS_Euler
from Plot import myPlot
import time
import sys
sys.setrecursionlimit(120500)

#data to change
n = 3
change_step = 2

#Prepare count table
X = []
X_for_all_Hamilton_paths = []
break_for_all_Hamilton_paths = 20
#Prepare time tables:
""" 2 """
searching_for_Euler_path_time_d06 = []
searching_for_one_Hamilton_path_time_d06 = []
searching_for_all_Hamilton_path_time_d06 = []

""" 3 """
searching_for_Euler_path_time_d02 = []
#searching_for_Euler_path_time_d06 = []         the same as previous

""" 4 """
searching_for_one_Hamilton_path_time_d02 = []
#searching_for_one_Hamilton_path_time_d06 = []  the same as previous
searching_for_all_Hamilton_path_time_d02 = []
#searching_for_all_Hamilton_path_time_d06 = []  the same as previous
Hamilton_paths_d02 = []
Hamilton_paths_d06 = []
Hamilton_paths_amount_d02 = []
Hamilton_paths_amount_d06 = []
"""________________________________________________________________________ """

for multiplier in range(1,31):
    if multiplier > break_for_all_Hamilton_paths:
        multiplier *= change_step
    
    am02 = makeEulerAM(multiplier * n, 0.2)          #AdjacencyMatrix d = 20%
    am06 = makeEulerAM(multiplier * n, 0.6)          #AdjacencyMatrix d = 60%
    al02 = makeAdjacencyList(am02)              #Adjacency list d = 20%
    al06 = makeAdjacencyList(am06)              #Adjacency list d = 60%

    
    
    X.append(multiplier * n)  
    
########################### 2 #################################################
    #Przedstawić w tabeli i na wspólnym wykresie zależności tE = f(n),
    #tH1 = f(n), tHA = f(n) dla d=0.6 (w razie konieczności należy zastosować 
    #skalę logarytmiczną). 
    
    start = time.time()          
    DFS_Euler(al06)    
    end = time.time()
    searching_for_Euler_path_time_d06.append(end - start) 
    
    start = time.time()          
    DFS_Hamilton_one(al06)    
    end = time.time()
    searching_for_one_Hamilton_path_time_d06.append(end - start) 
    
    if multiplier < break_for_all_Hamilton_paths:
        start = time.time()          
        Hamilton_paths_d06 = DFS_Hamilton_all(al06)    
        end = time.time()
        searching_for_all_Hamilton_path_time_d06.append(end - start) 
    else:
        searching_for_all_Hamilton_path_time_d06.append(0)

           
    
############################ 3 ################################################
#Przedstawić w tabeli i na wspólnym wykresie tE = f(n) dla różnych wartości d.
    
    start = time.time()          
    DFS_Euler(al02)    
    end = time.time()
    searching_for_Euler_path_time_d02.append(end - start) 
    

    #searching_for_Euler_path_time_d06     the same as previous
    #
    #
    #    
################################## 4 ##########################################
#Przedstawić w tabeli i na wspólnym wykresie tH1 = f(n) dla różnych wartości d 
#oraz na drugim wykresie tHA = f(n) dla różnych wartości d. Przedstawić
#w tabeli liczbę cykli cH. 
    
    

    start = time.time()          
    DFS_Hamilton_one(al02)    
    end = time.time()
    searching_for_one_Hamilton_path_time_d02.append(end - start) 
  
    #searching_for_one_Hamilton_path_time_d06 = []  the same as previous 
    #
    #
    #
    
    if multiplier < break_for_all_Hamilton_paths:
        start = time.time()          
        Hamilton_paths_d02 = DFS_Hamilton_all(al02)    
        end = time.time()
        searching_for_all_Hamilton_path_time_d02.append(end - start) 
        
        #searching_for_all_Hamilton_path_time_d06 = []  the same as previous
        #
        #
        #
        Hamilton_paths_amount_d02.append(len(Hamilton_paths_d02))
        Hamilton_paths_amount_d06.append(len(Hamilton_paths_d06))
        
        X_for_all_Hamilton_paths.append(multiplier * n) 
    else:
        searching_for_all_Hamilton_path_time_d02.append(0)
    
    print("Done ", multiplier / change_step, "/30")





###############################################################################
                                #Plot data
###############################################################################

### 1

legend = ["Gęstość 60%"]  
columnNames = ["Cykl Eulera", "Cykl Hamiltona", "Wszystkie cykle Hamiltona"]  
data = [searching_for_Euler_path_time_d06, 
         searching_for_one_Hamilton_path_time_d06,
         searching_for_all_Hamilton_path_time_d06]
x_label =  "Liczba wierzchołków"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń od liczby wierzchołków 
            dla gęstości grafu 60%"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)


### 2 
legend = ["Gęstość 20%", "Gęstość 60%"]
columnNames = ["Gęstość 20%", "Gęstość 60%"]
data = [searching_for_Euler_path_time_d02, searching_for_Euler_path_time_d06]
x_label =  "Ilość wierzchołków"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń cyklu Hamiltona od 
        gęstości grafu d = {20%, 60%}"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)



### 4
legend = ["Gęstość 20%", "Gęstość 60%"]
columnNames = ["Gęstość 20%", "Gęstość 60%"]
data = [searching_for_one_Hamilton_path_time_d02,
         searching_for_one_Hamilton_path_time_d06]
x_label =  "Ilość wierzchołków"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń jednego cyklu Hamiltona od 
        gęstości grafu d = {20%, 60%}"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)

legend = ["Gęstość 20%", "Gęstość 60%"]
columnNames = ["Gęstość 20%", "Gęstość 60%"]
data = [searching_for_all_Hamilton_path_time_d02[:19],
         searching_for_all_Hamilton_path_time_d06[:19]]
x_label =  "Ilość wierzchołków"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń wszystkich cykli Hamiltona od 
        gęstości grafu d = {20%, 60%}"""
myPlot(X_for_all_Hamilton_paths, 
       data, legend, columnNames, x_label, y_label, title)

legend = ["Gęstość 20%", "Gęstość 60%"]
columnNames = ["Gęstość 20%", "Gęstość 60%"]
data = [Hamilton_paths_amount_d02,
         Hamilton_paths_amount_d06]
x_label =  "Ilość wierzchołków"
y_label = "Ilość cykli"
title = """Zależność liczby cykli Hamiltona od 
        gęstości grafu d = {20%, 60%}"""
myPlot(X_for_all_Hamilton_paths, data, legend, columnNames, 
       x_label, y_label, title)













