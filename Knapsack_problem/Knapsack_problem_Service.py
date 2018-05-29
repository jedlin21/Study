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
from backtracking import backtracking
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
multiplier = 1
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

for m in range(1):
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

    for n in range(4,12):
        
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
        dynamic(multiplier * n ,b_05, weights, values)   
        end = time.time()
        dynnamic_time_b05.append(end - start) 
        
        start = time.time()          
        full(b_05, weights, values)    
        end = time.time()
        full_time_b05.append(end - start) 
        
        start = time.time()          
        backtracking(b_05, weights, values)    
        end = time.time()
        backtracking_time_b05.append(end - start) 
        
        start = time.time()          
        H_quotient_values_and_weights(tab_w_v, b_05)    
        end = time.time()
        H_division_time_b05.append(end - start) 
        
        
               
    ############################ 3 ############################################
    #Zbadać zależność czasu obliczeń t od liczby paczek n (minimum 
    #10 punktów pomiarowych) dla metody PD, BF1, BF2 i GH4 dla b = 25%Σs(ai) 
    #i 75%Σs(ai). Metody mogą być testowane niezależnie.
        """25%"""
        start = time.time()          
        dynamic(multiplier * n ,b_025, weights, values)   
        end = time.time()
        dynnamic_time_b025.append(end - start) 
        
        start = time.time()          
        full(b_025, weights, values)    
        end = time.time()
        full_time_b025.append(end - start) 
        
        start = time.time()          
        backtracking(b_025, weights, values)    
        end = time.time()
        backtracking_time_b025.append(end - start) 
        
        start = time.time()          
        H_quotient_values_and_weights(tab_w_v, b_025)    
        end = time.time()
        H_division_time_b025.append(end - start) 
        
        """75%"""
        start = time.time()          
        dynamic(multiplier * n ,b_075, weights, values)   
        end = time.time()
        dynnamic_time_b075.append(end - start) 
        
        start = time.time()          
        full(b_075, weights, values)    
        end = time.time()
        full_time_b075.append(end - start) 
        
        start = time.time()          
        backtracking(b_075, weights, values)    
        end = time.time()
        backtracking_time_b075.append(end - start) 
        
        start = time.time()          
        H_quotient_values_and_weights(tab_w_v, b_075)    
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
        H_random(tab_w_v, b_025)    
        end = time.time()
        H_random_time_b025.append(end - start)
        
        start = time.time()          
        H_min_weight_sort(tab_w_v, b_025)    
        end = time.time()
        H_weights_time_b025.append(end - start)
        
        start = time.time()          
        H_max_value_sort(tab_w_v, b_025)    
        end = time.time()
        H_values_time_b025.append(end - start)
    
        """50%"""
        start = time.time()          
        H_random(tab_w_v, b_05)    
        end = time.time()
        H_random_time_b05.append(end - start)
        
        start = time.time()          
        H_min_weight_sort(tab_w_v, b_05)    
        end = time.time()
        H_weights_time_b05.append(end - start)
        
        start = time.time()          
        H_max_value_sort(tab_w_v, b_05)    
        end = time.time()
        H_values_time_b05.append(end - start)
        
        """75%"""
        start = time.time()          
        H_random(tab_w_v, b_075)    
        end = time.time()
        H_random_time_b075.append(end - start)
        
        start = time.time()          
        H_min_weight_sort(tab_w_v, b_075)    
        end = time.time()
        H_weights_time_b075.append(end - start)
        
        start = time.time()          
        H_max_value_sort(tab_w_v, b_075)    
        end = time.time()
        H_values_time_b075.append(end - start)
        
        
    
        print("Done ", n, "/10")

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
        
        MEAN_H_random_time_b025 = H_random_time_b025[:]
        MEAN_H_weights_time_b025 = H_weights_time_b025[:]
        MEAN_H_values_time_b025 = H_values_time_b025[:]
        
        MEAN_H_random_time_b05 = H_random_time_b05[:]
        MEAN_H_weights_time_b05 = H_weights_time_b05[:]
        MEAN_H_values_time_b05 = H_values_time_b05[:]
        
        MEAN_H_random_time_b075 = H_random_time_b075[:]
        MEAN_H_weights_time_b075 = H_weights_time_b075[:]
        MEAN_H_values_time_b075 = H_values_time_b075[:]
        MEAN_flag = False
        """
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

legend = ["Algorytm dynamiczny", "Algorytm pełny", "Algorytm z powracaniem", 
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



### 4








