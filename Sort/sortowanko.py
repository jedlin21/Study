import random
import time
import matplotlib.pyplot as plt
import numpy as np

#Selection sort
def sortSS(tab):
    for x in range(len(tab)-1, -1 , -1):      #from end do start 
        maxel = tab[0]
        position = 0
        for i in range(x+1):               #find the maxest element 
            if tab[i] > maxel:
                maxel = tab[i]
                position = i
        tab[position], tab[x] = tab[x], tab[position]     #give elemenet to the end of table
    return tab

#Insertion sort
def sortIS(tab):
    for x in range(1,len(tab)):
        value = tab[x]
        position = x
        while position > 0 and tab[position - 1] > value:          #what?
            tab[position] = tab[position-1]
            position -= 1
        tab[position] = value
    return tab

#Bubble sort
def sortBS(tab):          
    for x in tab:
        for y in range(len(tab) - 1):
            if tab[y] > tab[y+1]:
                tab[y], tab[y+1] = tab[y+1], tab[y]      #change if tab[y] > tab[y+1]
    return tab
        


#Prepare to Heap sort
def buildHeap(tab, end, i):
    head = i
    left = 2 * i + 1        
    right = 2 * (i + 1)   
    max = head   
    if left < end and tab[head] < tab[left]:   #idex in table and left > head 
        max = left    
    if right < end and tab[max] < tab[right]:   #idex in table and right > max(head or left)
        max = right   
    if max != head:                            #if previous "if" was used
        tab[head], tab[max] = tab[max], tab[head]   #make change
        buildHeap(tab, end, max)                     #and build heap where change have been made
                                                     #index "max" is leaf after change. Now head value is there
#Heap sort
def sortHS(tab):
    end = len(tab)
    start = end // 2 - 1  #start from middle
    for i in range(start, -1, -1):   #from middle to first element build heap
        buildHeap(tab, end, i)
    for i in range(end-1, 0, -1):     #when heap is build
        tab[i], tab[0] = tab[0], tab[i]   #give largest element to the end 
        buildHeap(tab, i, 0)              #and build heap
    return tab

#merge sort
def sortMS(tab):
    result = []
    
    if len(tab) < 2:    #end of recusion
        return tab
    middle = len(tab) // 2
    leftTab = sortMS(tab[:middle])    #divide tabel to half
    rightTab = sortMS(tab[middle:])
    
    i = 0
    j = 0
    while i < len(leftTab) and j < len(rightTab):     #if index "i" and "j" is in the table 
        if leftTab[i] < rightTab[j]:                  #if elem i'th of left table is less than j'th elem of right elem
            result.append(leftTab[i])                  # take i'th elem
            i += 1                                     # and move i to next elem
        else:
            result.append(rightTab[j])
            j += 1
    result += leftTab[i:]   # if rightTab is empty add every leftTab element\
    result += rightTab[j:]   # if leftTab is empty add every rightTab element
    return result

#Counting sort
def sortCS(tab):      
    maxElem = max(tab)         
    C = [0]*(maxElem+1)          #prepare C
    Cprim = [0]*(maxElem+1)      #prepare Cprim
    for el in tab:              
        C[el] += 1
    Cprim[0] = C[0]
    for i in range(1, len(C)):
        Cprim[i] = Cprim[i - 1] + C[i]

    result = [0] * (len(tab)+1)
    for el in range(len(tab)-1, -1, -1):
        result[Cprim[tab[el]]] = tab[el]
        Cprim[tab[el]] -= 1
    return result[1:]
            

#how many elements
x = []
#sort time
ySS = []
yIS = []
yBS = []
yHS = []
yMS = []
yCS = []
#yQSMiddle = []
#yQSSide = []
yBuildIn = []

def makeData():
    for multiplier in range(1,11):
        tabRandom = []
        for elem in range (0, multiplier * 1000):                     #make table
            tabRandom.append(random.randint(0, multiplier * 1000)) #make table multiplier * 10,000 where multiplier[1,10]
        
        #prepare X
        x.append(multiplier * 1000)
    
        #prepare Y
        
        #Selection sort
        copyTable = tabRandom[:]
        start = time.time()
        sortSS(copyTable)
        end = time.time()
        ySS.append(end - start)
        
        #Insertion sort
        copyTable = tabRandom[:]
        start = time.time()
        sortIS(copyTable)
        end = time.time()
        yIS.append(end - start)
        
        #Bubble sort
        copyTable = tabRandom[:]
        start = time.time()
        sortBS(copyTable)
        end = time.time()
        yBS.append(end - start)
        
        #Heap sort
        copyTable = tabRandom[:]
        start = time.time()
        sortHS(copyTable)
        end = time.time()
        yHS.append(end - start)
        
        #Merge sort
        copyTable = tabRandom[:]
        start = time.time()
        sortMS(copyTable)
        end = time.time()
        yMS.append(end - start)
        
        #counting sort
        copyTable = tabRandom[:]
        start = time.time()
        sortCS(copyTable)
        end = time.time()
        yCS.append(end - start)
        
        #buid in merge
        copyTable = tabRandom[:]
        start = time.time()
        sorted(copyTable)
        end = time.time()
        yBuildIn.append(end - start)
        
        print("done", multiplier)


makeData()
print(x, ySS, yIS, yBS, yHS, yMS, yCS)

#plot
plt.plot(x, ySS)
plt.plot(x, yIS)
plt.plot(x, yBS)
plt.plot(x, yHS)
plt.plot(x, yMS)
plt.plot(x, yCS)

plt.legend(['SS', 'IS', 'BS', 'HS', 'MS', 'CS'], loc='upper left')
plt.show()

#plot
plt.plot(x, yHS)
plt.plot(x, yMS)
plt.plot(x, yCS)
plt.plot(x, yBuildIn)

plt.legend(['HS', 'MS', 'CS','buidin'], loc='upper left')
plt.show()
























