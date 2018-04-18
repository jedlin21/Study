import sys
import random
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(12500)
tabRandom = []

for x in range (0, 10):
    tabRandom.append(random.randint(0, 10))
print(type(random.randint(0, 10)))
#Selection sort
def sortSS(tab):
    for x in range(len(tab)-1, -1 , -1):      #from end do start 
        maxel = tab[0]
        position = 0
        for i in range(x+1):               #find maximal element
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
        while position > 0 and tab[position - 1] > value:         
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
    
    if len(tab) < 2:    #end of recursion
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

#Quick sort(side)
def sortQSside(tab):
    QSHelper(tab,0,len(tab)-1)
def QSHelper(tab,first,last):
    if first<last:                                  #jeśli fragment tablicy dłuższy niż jeden element
        splitpoint=partition(tab,first,last)        #dzieli i zapamiętuje punkt podziału(splitpoint)
        QSHelper(tab,first,splitpoint-1)            #sortuje lewą część
        QSHelper(tab,splitpoint+1,last)             #sortuje prawą część
def partition(tab,first,last):
    pivot = tab[first]              #element służący do podziału tablicy (tutaj pierwszy element tablicy)
    left = first+1
    right = last
    done = False
    while not done:
        while left<=right and tab[left]<=pivot:
            left += 1
        while tab[right]>=pivot and right>=left:
            right -= 1
        if right<left:
            done=True
        else:
            tab[left], tab[right] = tab[right], tab[left]
    tab[first], tab[right] = tab[right], tab[first]
    return right

# Quick sort(middle)
def sortQSmiddle(tab, left=0, right=None):          #podobnie jak poprzedni QS tylko ze zmianą miejsca podziału i zwięźlej zapisany
    if right is None: right = len(tab) - 1
    i, j = left, right
    pivot = tab[(left + right) // 2]
    while i <= j:
        while tab[i] < pivot: i += 1
        while tab[j] > pivot: j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1; j -= 1
    if left < j: sortQSmiddle(tab, left, j)
    if right > i: sortQSmiddle(tab, i, right)

print(tabRandom)
sortQSmiddle(tabRandom)
print(tabRandom)

#how many elements
x = []
#sort time
ySS = []
yIS = []
yBS = []
yHS = []
yMS = []
yCS = []
yQSmiddle = []
yQSside = []

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
    
        #quicksort side
        copyTable = tabRandom[:]
        start = time.time()
        sortQSside(copyTable)
        end = time.time()
        yQSside.append(end - start)
    
        #quicksort middle
        copyTable = tabRandom[:]
        start = time.time()
        sortQSmiddle(copyTable)
        end = time.time()
        yQSmiddle.append(end - start)
    
    
        print("done")


def makeThirdData():
    for multiplier in range(1,11):
        tabGrow = []
        for elem in range (0, multiplier * 1000):                     #make table
            tabGrow.append(elem) #make table multiplier * 10,000 where multiplier[1,10]
            
            
        #prepare X
        x.append(multiplier * 1000)
        
        #Insertion sort
        copyTable = tabGrow[:]
        start = time.time()
        sortIS(copyTable)
        end = time.time()
        yIS.append(end - start)
    
        #quicksort side
        copyTable = tabGrow[:]
        start = time.time()
        sortQSside(copyTable)
        end = time.time()
        yQSside.append(end - start)
    
        #quicksort middle
        copyTable = tabGrow[:]
        start = time.time()
        sortQSmiddle(copyTable)
        end = time.time()
        yQSmiddle.append(end - start)
        
        print('Done', multiplier)
        print(tabGrow[:20], len(tabGrow))
        
        
    
def plotForAll():
    plt.plot(x, ySS)
    plt.plot(x, yIS)
    plt.plot(x, yBS)
    plt.plot(x, yHS)
    plt.plot(x, yMS)
    plt.plot(x, yCS)
    plt.plot(x, yQSside)
    plt.plot(x, yQSmiddle)
    plt.legend(['SS', 'IS', 'BS', 'HS', 'MS', 'CS', 'QSside', 'QSmiddle'], loc='upper left')
    plt.show()

def plotThird():
    plt.plot(x, yIS)
    plt.plot(x, yQSside)
    plt.plot(x, yQSmiddle)
    plt.legend(['IS', 'QSside', 'QSmiddle'], loc='upper left')
    plt.show()
    
def makeFourthData(n = 0):
    for multiplier in range(1,11):
        tabRandom = []
        if(n == 0):
            for elem in range (0, multiplier * 100000):                     
                tabRandom.append(random.randint(0, multiplier * 100000 * 100))
        
        if(n == 1):
            for elem in range (0, multiplier * 100000):                     
                tabRandom.append(random.randint(0, multiplier * 100000 / 100))
            
            
            
        #prepare X
        x.append(multiplier * 100000)
        
        #counting sort
        copyTable = tabRandom[:]
        start = time.time()
        sortCS(copyTable)
        end = time.time()
        yCS.append(end - start)
    
        #quicksort middle
        copyTable = tabRandom[:]
        start = time.time()
        sortQSmiddle(copyTable)
        end = time.time()
        yQSmiddle.append(end - start)
        
        print('Done', multiplier)
        print(tabRandom[:20], len(tabRandom), max(tabRandom))


def plotFourth():
    plt.plot(x, yCS)
    plt.plot(x, yQSmiddle)
    plt.legend(['CS', 'QSmiddle'], loc='upper left')
    plt.show()

makeData()
plotForAll()
#makeThirdData()
#plotThird()
#makeFourthData()
#plotFourth()
    
    








































