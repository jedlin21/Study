import time
import matplotlib.pyplot as plt
import numpy as np

#Selection sort
def sortSS(tab):
    for x in range(len(tab), 0 , -1):      #from end do start 
        position = np.argmax(tab[:x])
        tab[position], tab[x-1] = tab[x-1], tab[position]     #give elemenet to the end of table
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
    print(type(tab))          
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
    end = tab.size
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
    middle = tab.size // 2
    leftTab = sortMS(tab[:middle])    #divide tabel to half
    rightTab = sortMS(tab[middle:])
    
    i = 0
    j = 0
    while i < leftTab.size and j < rightTab.size:     #if index "i" and "j" is in the table 
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
    C = np.zeros(maxElem+1)          #prepare C
    Cprim = np.zeros(maxElem+1)      #prepare Cprim
    for el in tab:              
        C[el] += 1
    Cprim[0] = C[0]
    for i in range(1, len(C)):
        Cprim[i] = Cprim[i - 1] + C[i]

    result = np.zeros(len(tab)+1)
    for el in range(len(tab)-1, -1, -1):
        result[Cprim[tab[el]]] = tab[el]
        Cprim[tab[el]] -= 1
    return result[1:]
            
tab1 = np.random.randint(10, size=10)
tab1[9] = 11
print(tab1)
print(sortBS(tab1))



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


tabRandom = []
#how many elements
x = []
#sort time
ySS = []
yIS = []
yBS = []
yHS = []
yMS = []
yCS = []





def makeDataNumpy():
    for multiplier in range(1,11):
        tabRandom = np.random.randint(1000*multiplier, size=1000*multiplier) #make table multiplier * 1,000 where multiplier[1,10]
        
        #prepare X
        x.append(multiplier * 1000)
    
        ###prepare Y
        
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
        
        print("done")




def CheckNumpy():
    for multiplier in range(1,11):
        tabRandom = np.random.randint(1000*multiplier, size=1000*multiplier) #make table multiplier * 1,000 where multiplier[1,10]
        
        #prepare X
        x.append(multiplier * 1000)

        
        #Bubble sort
        copyTable = tabRandom[:]
        start = time.time()
        sortBS(copyTable)
        end = time.time()
        yBS.append(end - start)



CheckNumpy()
#makeDataNumpy()
#print(x, ySS, yIS, yBS, yHS, yMS, yCS)

def plotAll()
    #plot
    plt.plot(x, ySS)
    plt.plot(x, yIS)
    plt.plot(x, yBS)
    plt.plot(x, yHS)
    plt.plot(x, yMS)
    plt.plot(x, yCS)
    plt.show()

def plotOne():
    plt.plot(x, yBS)
    plt.show()
















