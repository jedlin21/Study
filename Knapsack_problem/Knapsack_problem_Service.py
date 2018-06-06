#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:13:57 2018

@author: i
"""
from full import full
from dynamic import (find_the_best_indexes,
                     dynamic)
from weightAndValues import make_Weights_and_values
from backtracking_faster import back
from full_second import full_second
from Heurustics import (make_tab, 
                        H_random,
                        H_min_weight_sort,
                        H_max_value_sort,
                        H_quotient_values_and_weights)
from Plot import myPlot
import pandas as pd
import time
import sys
sys.setrecursionlimit(2 ** 30)
import threading
threading.stack_size(6710886400) # 64MB * 100 stack

#data to change
cycles = 1    #hom many repeats
multiplier = 2
step = 2 

max_weight = 1000
max_value = 10000

#MEAN DATA
MEAN_flag = True
""" 2 """
MEAN_dynnamic_time_b05 = []
MEAN_full_time_b05 = []
MEAN_backtracking_time_b05 = []
MEAN_H_division_time_b05 = []

""" 3 """
MEAN_dynnamic_time_b025 = []
MEAN_full_time_b025 = []
MEAN_backtracking_time_b025 = []
MEAN_H_division_time_b025 = []

MEAN_dynnamic_time_b075 = []
MEAN_full_time_b075 = []
MEAN_backtracking_time_b075 = []
MEAN_H_division_time_b075 = []


""" 4 """
MEAN_H_random_time_b025 = []
MEAN_H_weights_time_b025 = []
MEAN_H_values_time_b025 = []
#H_division_time_b025 = []
#dynnamic_time_b025 = []

MEAN_H_random_time_b05 = []
MEAN_H_weights_time_b05 = []
MEAN_H_values_time_b05 = []
#H_division_time_b025 = []
#dynnamic_time_b05 = []

MEAN_H_random_time_b075 = []
MEAN_H_weights_time_b075 = []
MEAN_H_values_time_b075 = []
#H_division_time_b025 = []
#dynnamic_time_b075 = []

random_mistake_025 = []
min_weight_mistake_025 = [] 
max_value_mistake_025 = []
quotient_mistake_025 = []

random_mistake_05  = []
min_weight_mistake_05  = []
max_value_mistake_05 = []
quotient_mistake_05 = []

random_mistake_075  = []
min_weight_mistake_075 = [] 
max_value_mistake_075 = []
quotient_mistake_075  = []

mean_random = []
mean_min_weight = [] 
mean_max_value = []
mean_quotient = []
        

for m in range(cycles):
    #Prepare count table
    X = []
    
    #Prepare time tables:
    """ 2 """
    dynnamic_time_b05 = []
    full_time_b05 = []
    backtracking_time_b05 = []
    H_division_time_b05 = []

    """ 3 """
    dynnamic_time_b025 = []
    full_time_b025 = []
    backtracking_time_b025 = []
    H_division_time_b025 = []
    
    dynnamic_time_b075 = []
    full_time_b075 = []
    backtracking_time_b075 = []
    H_division_time_b075 = []

    
    """ 4 """
    H_random_time_b025 = []
    H_weights_time_b025 = []
    H_values_time_b025 = []
    #H_division_time_b025 = []
    #dynnamic_time_b025 = []
    
    H_random_time_b05 = []
    H_weights_time_b05 = []
    H_values_time_b05 = []
    #H_division_time_b025 = []
    #dynnamic_time_b05 = []
    
    H_random_time_b075 = []
    H_weights_time_b075 = []
    H_values_time_b075 = []
    #H_division_time_b025 = []
    #dynnamic_time_b075 = []
    
    
    
    """_____________________________________________________________________ """

    for n in range(2,13):
        if n > 10:
            multiplier = step
        
        weights, values = make_Weights_and_values(multiplier * n, 
                                                  max_weight, 
                                                  max_value)
        b_025 = int(0.25 * sum(weights))
        b_05 = 2 * b_025
        b_075 = b_05 + b_025
    
        tab_w_v = make_tab(weights, values)
        X.append(multiplier * n)  
        
    ########################### 2 #############################################
        #Zbadać zależność czasu obliczeń t od liczby paczek n (minimum 
        #10 punktów pomiarowych dostosowanych do wymagań czasowych BF) dla 
        #metody PD, BF1, BF2 i GH4 dla b = 50%Σs(ai).
            
    
        start = time.time()          
        profit_max_05 = dynamic(multiplier * n ,b_05, weights, values)   
        end = time.time()
        dynnamic_time_b05.append(end - start) 
        
        if n <= 10:
            start = time.time()          
            full(b_05, weights, values)    
            end = time.time()
            full_time_b05.append(end - start) 
        else:
            full_time_b05.append(0)
        
        start = time.time()          
        back(tab_w_v, b_05)    
        end = time.time()
        backtracking_time_b05.append(end - start) 
        
        start = time.time()          
        sequence, profit_quotient_05 = H_quotient_values_and_weights(tab_w_v,
                                                                       b_05)    
        end = time.time()
        H_division_time_b05.append(end - start) 
        
        
               
    ############################ 3 ############################################
    #Zbadać zależność czasu obliczeń t od liczby paczek n (minimum 
    #10 punktów pomiarowych) dla metody PD, BF1, BF2 i GH4 dla b = 25%Σs(ai) 
    #i 75%Σs(ai). Metody mogą być testowane niezależnie.
        """25%"""
        start = time.time()          
        profit_max_025 = dynamic(multiplier * n ,b_025, weights, values)   
        end = time.time()
        dynnamic_time_b025.append(end - start) 
        
        if n <= 10:
            start = time.time()          
            full(b_025, weights, values)    
            end = time.time()
            full_time_b025.append(end - start) 
        else:
            full_time_b025.append(0)
        
        start = time.time()          
        back(tab_w_v, b_025)    
        end = time.time()
        backtracking_time_b025.append(end - start) 
        
        start = time.time()          
        sequence, profit_quotient_025 = H_quotient_values_and_weights(tab_w_v, 
                                                                      b_025)    
        end = time.time()
        H_division_time_b025.append(end - start) 
        
        """75%"""
        start = time.time()          
        profit_max_075 = dynamic(multiplier * n ,b_075, weights, values)   
        end = time.time()
        dynnamic_time_b075.append(end - start) 
        
        if n <= 10:
            start = time.time()          
            full(b_075, weights, values)    
            end = time.time()
            full_time_b075.append(end - start) 
        else:
            full_time_b075.append(0)
        
        start = time.time()          
        back(tab_w_v, b_075)    
        end = time.time()
        backtracking_time_b075.append(end - start) 
        
        start = time.time()          
        sequence, profit_quotient_075 =  H_quotient_values_and_weights(tab_w_v, 
                                                                       b_075)    
        end = time.time()
        H_division_time_b075.append(end - start) 
        
        
    ################################## 4 ##########################################
    #Wyznaczyć rozwiązanie problemu za pomocą metody PD, GH1, GH2, GH3 i GH4 
    #dla minimum 10 wartości n (dobranych do czasu działania metod) 
    #i b = 25%Σs(ai), 50%Σs(ai) i 75%Σs(ai). Obliczyć średni błąd popełniany
    #przez poszczególne heurystyki dla różnych b (tzn. średnia 
    #(xPD-xGH)/xPD*100% po n dla danej wartości b, gdzie xA oznacza wartość 
    #rozwiązania dla metody A) i w całym eksperymencie.
        
        """25%"""
        start = time.time()          
        sequence, profit_random_025 = H_random(tab_w_v, b_025)    
        end = time.time()
        H_random_time_b025.append(end - start)
        
        start = time.time()          
        sequence, profit_min_weight_025 = H_min_weight_sort(tab_w_v, b_025)    
        end = time.time()
        H_weights_time_b025.append(end - start)
        
        start = time.time()          
        sequence, profit_max_value_025 = H_max_value_sort(tab_w_v, b_025)    
        end = time.time()
        H_values_time_b025.append(end - start)
    
        """50%"""
        start = time.time()          
        sequence, profit_random_05 = H_random(tab_w_v, b_05)    
        end = time.time()
        H_random_time_b05.append(end - start)
        
        start = time.time()          
        sequence, profit_min_weight_05 = H_min_weight_sort(tab_w_v, b_05)    
        end = time.time()
        H_weights_time_b05.append(end - start)
        
        start = time.time()          
        sequence, profit_max_value_05 = H_max_value_sort(tab_w_v, b_05)    
        end = time.time()
        H_values_time_b05.append(end - start)
        
        """75%"""
        start = time.time()          
        sequence, profit_random_075 = H_random(tab_w_v, b_075)    
        end = time.time()
        H_random_time_b075.append(end - start)
        
        start = time.time()          
        sequence, profit_min_weight_075 = H_min_weight_sort(tab_w_v, b_075)    
        end = time.time()
        H_weights_time_b075.append(end - start)
        
        start = time.time()          
        sequence, profit_max_value_075 = H_max_value_sort(tab_w_v, b_075)    
        end = time.time()
        H_values_time_b075.append(end - start)
        
        """Calculations"""
        random_mistake_025.append(((profit_max_025 - profit_random_025) 
                              / profit_max_025) * 100)
        min_weight_mistake_025.append(((profit_max_025 - profit_min_weight_025) 
                                / profit_max_025) * 100)
        max_value_mistake_025.append(((profit_max_025 - profit_max_value_025)
                                / profit_max_025) * 100)
        quotient_mistake_025.append(((profit_max_025 - profit_quotient_025) 
                               / profit_max_025) * 100)
        
        random_mistake_05.append(((profit_max_05 - profit_random_05) 
                            / profit_max_05) * 100)
        min_weight_mistake_05.append(((profit_max_05 - profit_min_weight_05) 
                                / profit_max_05) * 100)
        max_value_mistake_05.append(((profit_max_05 - profit_max_value_05) 
                               / profit_max_05) * 100)
        quotient_mistake_05.append(((profit_max_05 - profit_quotient_05) 
                              / profit_max_05) * 100)
        
        random_mistake_075.append(((profit_max_075 - profit_random_075)
                             / profit_max_075) * 100)
        min_weight_mistake_075.append(((profit_max_075 - profit_min_weight_075) 
                                 / profit_max_075) * 100)
        max_value_mistake_075.append(((profit_max_075 - profit_max_value_075) 
                                / profit_max_075) * 100)
        quotient_mistake_075.append(((profit_max_075 - profit_quotient_075) 
                               / profit_max_075) * 100)
        

        
    
        print("Done ", n - 1, "/20")

#MEAN
    if MEAN_flag:
        MEAN_dynnamic_time_b05 = dynnamic_time_b05[:]
        MEAN_full_time_b05 = full_time_b05[:]
        MEAN_backtracking_time_b05 = backtracking_time_b05[:]
        MEAN_H_division_time_b05 = H_division_time_b05[:]
        
        MEAN_dynnamic_time_b025 = dynnamic_time_b025[:]
        MEAN_full_time_b025 = full_time_b025[:]
        MEAN_backtracking_time_b025 = backtracking_time_b025[:]
        MEAN_H_division_time_b025 = H_division_time_b025[:]
        
        MEAN_dynnamic_time_b075 = dynnamic_time_b075[:]
        MEAN_full_time_b075 = full_time_b075[:]
        MEAN_backtracking_time_b075 = backtracking_time_b075[:]
        MEAN_H_division_time_b075 = H_division_time_b075[:]
        
        """
        MEAN_H_random_time_b025 = H_random_time_b025[:]
        MEAN_H_weights_time_b025 = H_weights_time_b025[:]
        MEAN_H_values_time_b025 = H_values_time_b025[:]
        
        MEAN_H_random_time_b05 = H_random_time_b05[:]
        MEAN_H_weights_time_b05 = H_weights_time_b05[:]
        MEAN_H_values_time_b05 = H_values_time_b05[:]
        
        MEAN_H_random_time_b075 = H_random_time_b075[:]
        MEAN_H_weights_time_b075 = H_weights_time_b075[:]
        MEAN_H_values_time_b075 = H_values_time_b075[:]
        """
        
        
        MEAN_flag = False
    else:
        l = [MEAN_dynnamic_time_b05[:], dynnamic_time_b05[:]]
        MEAN_dynnamic_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_full_time_b05, full_time_b05[:]]
        MEAN_full_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_backtracking_time_b05, backtracking_time_b05[:]]
        MEAN_backtracking_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_division_time_b05, H_division_time_b05[:]]
        MEAN_H_division_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        
        l = [MEAN_dynnamic_time_b025[:], dynnamic_time_b025[:]]
        MEAN_dynnamic_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_full_time_b025, full_time_b025[:]]
        MEAN_full_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_backtracking_time_b025, backtracking_time_b025[:]]
        MEAN_backtracking_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_division_time_b025, H_division_time_b025[:]]
        MEAN_H_division_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        
        l = [MEAN_dynnamic_time_b075[:], dynnamic_time_b075[:]]
        MEAN_dynnamic_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_full_time_b075, full_time_b05[:]]
        MEAN_full_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_backtracking_time_b075, backtracking_time_b075[:]]
        MEAN_backtracking_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_division_time_b075, H_division_time_b075[:]]
        MEAN_H_division_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        
        
        """
        l = [MEAN_H_random_time_b025[:], H_random_time_b025[:]]
        MEAN_H_random_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_weights_time_b025, H_weights_time_b025[:]]
        MEAN_H_weights_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_values_time_b025, H_values_time_b025[:]]
        MEAN_H_values_time_b025 = [(x+y)/2 for x,y in zip(*l)]
        
        l = [MEAN_H_random_time_b05[:], H_random_time_b05[:]]
        MEAN_H_random_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_weights_time_b05, H_weights_time_b05[:]]
        MEAN_H_weights_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_values_time_b05, H_values_time_b05[:]]
        MEAN_H_values_time_b05 = [(x+y)/2 for x,y in zip(*l)]
        
        l = [MEAN_H_random_time_b075[:], H_random_time_b075[:]]
        MEAN_H_random_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_weights_time_b075, H_weights_time_b075[:]]
        MEAN_H_weights_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        l = [MEAN_H_values_time_b075, H_values_time_b075[:]]
        MEAN_H_values_time_b075 = [(x+y)/2 for x,y in zip(*l)]
        """

MEAN_random_mistake_025 = sum(random_mistake_025) / len(random_mistake_025) 
MEAN_min_weight_mistake_025 = sum(min_weight_mistake_025) / len(min_weight_mistake_025) 
MEAN_max_value_mistake_025 = sum(max_value_mistake_025) / len(max_value_mistake_025) 
MEAN_quotient_mistake_025 = sum(quotient_mistake_025) / len(quotient_mistake_025) 

MEAN_random_mistake_05 = sum(random_mistake_05) / len(random_mistake_05) 
MEAN_min_weight_mistake_05 = sum(min_weight_mistake_05) / len(min_weight_mistake_05) 
MEAN_max_value_mistake_05 = sum(max_value_mistake_05) / len(max_value_mistake_05) 
MEAN_quotient_mistake_05 = sum(quotient_mistake_05) / len(quotient_mistake_05) 

MEAN_random_mistake_075 = sum(random_mistake_075) / len(random_mistake_075) 
MEAN_min_weight_mistake_075 = sum(min_weight_mistake_075) / len(min_weight_mistake_075) 
MEAN_max_value_mistake_075 = sum(max_value_mistake_075) / len(max_value_mistake_075) 
MEAN_quotient_mistake_075 = sum(quotient_mistake_075) / len(quotient_mistake_075) 

MEAN_random = (sum(random_mistake_025) / len(random_mistake_025)
                + sum(random_mistake_05)/ len(random_mistake_05)
                + sum(random_mistake_075)/ len(random_mistake_075)) / 3

MEAN_min_weight = (sum(min_weight_mistake_025) / len(min_weight_mistake_025)
                  + sum(min_weight_mistake_05) / len(min_weight_mistake_05) 
                  + sum(min_weight_mistake_075) / len(min_weight_mistake_075)) / 3

MEAN_max_value = (sum(max_value_mistake_025) / len(max_value_mistake_025) 
                + sum(max_value_mistake_05) / len(max_value_mistake_05) 
                + sum(max_value_mistake_075) / len(max_value_mistake_075)) / 3

MEAN_quotient = (sum(quotient_mistake_025) / len(quotient_mistake_025)  
                + sum(quotient_mistake_05) / len(quotient_mistake_05)  
                + sum(quotient_mistake_075) / len(quotient_mistake_075)) / 3
        
        
###############################################################################
                                #Save data
###############################################################################
"""
data = pd.DataFrame([MEAN_searching_for_Euler_path_time_d06, 
         MEAN_searching_for_one_Hamilton_path_time_d06,
         MEAN_searching_for_all_Hamilton_path_time_d06])  
data.to_csv('./data/2.csv') 

data = pd.DataFrame([MEAN_searching_for_Euler_path_time_d02, 
                    MEAN_searching_for_Euler_path_time_d06])  
data.to_csv('./data/3.csv') 

data = pd.DataFrame([MEAN_searching_for_one_Hamilton_path_time_d02,
         MEAN_searching_for_one_Hamilton_path_time_d06]) 
data.to_csv('./data/4.1.csv') 

data = pd.DataFrame([MEAN_searching_for_all_Hamilton_path_time_d02,
                    MEAN_searching_for_all_Hamilton_path_time_d06])
data.to_csv('./data/4.2.csv')   

data = pd.DataFrame([Hamilton_paths_amount_d02,
         Hamilton_paths_amount_d06])  
data.to_csv('./data/4.3.csv')                             
""" 
###############################################################################
                                #Plot data
###############################################################################

### 1

legend = ["Algorytm dynamiczny", "Pełny przegląd", "Algorytm z powracaniem", 
          "Heurystyka iloczyn wagi i wartości"]  
columnNames = legend  
data = [MEAN_dynnamic_time_b05,
        MEAN_full_time_b05,
        MEAN_backtracking_time_b05,
        MEAN_H_division_time_b05]
x_label =  "Liczba paczek"
y_label = "Czas [s]"
title = "Zależność czasu trwania obliczeń od liczby paczek dla b = 50%"
myPlot(X, data, legend, columnNames, x_label, y_label, title)


### 2 

legend = ["Algorytm dynamiczny b = 25%", "Algorytm dynamiczny b = 75%"]  
columnNames = legend  
data = [MEAN_dynnamic_time_b025,
        MEAN_dynnamic_time_b075]
x_label =  "Liczba paczek"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń od liczby paczek dla algorymtu
          dynamicznego przy różnych pojemnościach plecaka"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)

legend = ["Pełny przegląd b = 25%", "Pełny przegląd b = 75%"]  
columnNames = legend  
data = [MEAN_full_time_b025,
        MEAN_full_time_b075]
x_label =  "Liczba paczek"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń od liczby paczek dla
            pełnego przeglądu przy różnych pojemnościach plecaka"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)

legend = ["Algorytm z powracaniem b = 25%", "Algorytm z powracaniem b = 75%"]  
columnNames = legend  
data = [MEAN_backtracking_time_b025,
        MEAN_backtracking_time_b075]
x_label =  "Liczba paczek"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń od liczby paczek dla algorymtu
          z powracaniem przy różnych pojemnościach plecaka"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)

legend = ["Heurystyka iloczyn wagi i wartości b = 25%", 
          "Heurystyka iloczyn wagi i wartości b = 75%"]  
columnNames = legend  
data = [MEAN_H_division_time_b025,
        MEAN_H_division_time_b075]
x_label =  "Liczba paczek"
y_label = "Czas [s]"
title = """Zależność czasu trwania obliczeń od liczby paczek dla heurystyki 
          iloczynu wagi i wartości przy różnych pojemnościach plecaka"""
myPlot(X, data, legend, columnNames, x_label, y_label, title)



### 4

#Prepare data
columnNames = ["GH1[%]", "GH2[%]", "GH3[%]", "GH4[%]"]
x = ["b = 25%","b = 50%","b = 75%","średnia"]
GH1_data = [MEAN_random_mistake_025, 
            MEAN_random_mistake_05,
            MEAN_random_mistake_075,
            MEAN_random]
GH2_data = [MEAN_min_weight_mistake_025,
            MEAN_min_weight_mistake_05,
            MEAN_min_weight_mistake_075,
            MEAN_min_weight]
GH3_data = [MEAN_max_value_mistake_025,
            MEAN_max_value_mistake_05,
            MEAN_max_value_mistake_075,
            MEAN_max_value]
GH4_data = [MEAN_quotient_mistake_025,
            MEAN_quotient_mistake_05,
            MEAN_quotient_mistake_075,
            MEAN_quotient]
data = [GH1_data, GH2_data, GH3_data, GH4_data]

#Show tables
d = {}
for name, y in zip(columnNames, data):
    d[name] = y
print(pd.DataFrame(data=d, index=x))





