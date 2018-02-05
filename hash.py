import numpy as np  #pip install numpy
#from numpy import array
from functools import reduce

def factors(n):
    return reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))


def googleHash(filename):
    with open(filename) as dataset:
        #Manipulating the first line from the dataset
        first_line = dataset.readline()
        first_line = first_line.strip('\n')
        requirements = first_line.split(" ") #Creating a list from 1st line
        print requirements
        print 'Requirement \n', \
        'From %s Rows of %s columns input dataset, creating slices with minimum of %s\
 of each ingredient per slice and maximum %s cells per slice. \n' \
         % (requirements[0], requirements[1], requirements[2], requirements[3])

        #Then, the remaining lines
        countM = 0
        countT = 0
        rowcount = 0
        #theArray = np.random.randn(int(requirements[0]),int(requirements[1]))
        theArray = np.empty(shape=(int(requirements[0]),int(requirements[1])))
        for line in dataset:
            #line = line.split
            lineList = []
            count = 0
            while count < int(requirements[1]):
                if str(line[count]) == "M":
                    countM+=1
                if str(line[count]) == "T":
                    countT+=1
                lineList.append(line[count])
                count+=1
            #print lineList
            for i in range (int(requirements[1])):
                if lineList[i] == "T" :
                    lineList[i] = 0
                if lineList[i] == "M" :
                    lineList[i] = 1
            #print lineList
            theArray[rowcount] = np.array(lineList, dtype=str)

            rowcount+=1
        print theArray, theArray.shape
        #print mynum

        print ' %s numbers of \'M\' \n %s numbers of \'T\' ' % (countM, countT)

        #Manipulating the numpy array, theArray
        #test1 = theArray[:5, :5]
        #print test1
        n = int(requirements[3])
        #print n
        rectList = factors(n)
        print len(rectList)

        factorsKey, factorsValue = rectList[::2], rectList[1::2]
        factorsDict = dict(zip(factorsKey, factorsValue)) #Mosudi: Create a dictionary factors
        print factorsDict

        rectListcount = 0
        while rectListcount < len(rectList) :
            print rectList[rectListcount]
            pizzarow = int(rectList[rectListcount])
            rectListcount+=1
            print rectList[rectListcount]
            pizzacol = int(rectList[rectListcount])
            pizzaArray = theArray[:pizzarow, :pizzacol]
            print pizzaArray
            rectListcount+=1










#filename = 'example.in'
#filename = 'small.in'
filename = 'medium.in'
googleHash(filename)
