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
                    lineList[i] = 1
                if lineList[i] == "M" :
                    lineList[i] = 0
            #print lineList
            theArray[rowcount] = np.array(lineList, dtype=str)
            rowcount+=1
            
        print theArray, theArray.shape
        #print mynum

        print ' %s numbers of \'M\' \n %s numbers of \'T\' ' % (countM, countT)


        n = int(requirements[3])
        #print n
        rectList = factors(n)
        #print len(rectList)

        #Creating Dictionary for the possible rectanglar slices
        factorsKey, factorsValue = rectList[::2], rectList[1::2]
        factorsDict = dict(zip(factorsKey, factorsValue)) #Mosudi: Create a dictionary factors
        print factorsDict


        """#Manipulating the Dictionary
                                for key, value in factorsDict.iteritems():
                                    pizzaArray = theArray[:key, :value]
                                    #print pizzaArray
                                    for v in range(int(requirements[1])):
                                        #print key, v
                                        #print theArray[:key, :v], theArray[:key, :v].shape
                                        sliceSize = np.sum(theArray[:key, :v])
                                        #print int(sliceSize), "\n"
                                        #print theArray[:v, :key], theArray[:v, :key].shape
                                        sliceSize = np.sum(theArray[:v, :key])
                                        #print int(sliceSize), "\n\n"
                                        v+=v
                                #print theArray, theArray.shape, "\n\n"
                        
                        """
        #theArray[startrow:endrow+1, starcol:endcol+1]
        #print theArray[0:3, 0:2], "0 0 3 2", "\n"
        for key, value in factorsDict.iteritems():

            valueRow=value
            keyCol = key
            initialCol=0
            initialRow=0
            rowwidth = 0
            colwidth = 0
            n = 1
            #print theArray[initialRow:valueRow, initialCol:keyCol]
            #sumUp=np.sum(theArray[initialRow:valueRow, initialCol:keyCol])
            #print int(sumUp), (keyCol - initialCol )* (valueRow- initialRow)
            sumUp = int(requirements[3]) - int(requirements[2])
            sliceNameList = []

            while keyCol*valueRow - int(requirements[2]) >= sumUp and \
            sumUp > int(requirements[2]) and keyCol > initialCol :

                
                newArray ='Slice' + str(n) 
                exec("%s = %d" % (newArray,2))
                #newArray = np.empty(shape=(valueRow, keyCol))
                #print initialCol, keyCol
                newArray=theArray[initialRow:valueRow, initialCol:keyCol]
                #sliceNameList.append(newArray)
                #print theArray[initialRow:valueRow, initialCol:keyCol]
                print newArray
                #sumUp=np.sum(theArray[initialRow:valueRow, initialCol:keyCol])
                sumUp=np.sum(newArray)
                print int(sumUp), (keyCol - initialCol )* (valueRow- initialRow), "\n", \
                initialRow, initialCol, valueRow, keyCol
                #rowsize = int(theArray[initialRow:valueRow, initialCol:keyCol].shape[0])
                #colsize = int(theArray[initialRow:valueRow, initialCol:keyCol].shape[1])
                rowsize = int(newArray.shape[0])
                colsize = int(newArray.shape[1])
                if colsize*rowsize == sumUp:
                    print "No way"


                #rowwidth+=rowsize
                colwidth+=colsize
                print str(rowsize)  + "    rowsize     " + str(colsize)   + "  colsize"
                print "colwidth  " + str(colwidth) 

                print "True"
                initialCol=keyCol
                keyCol+=1
                n+=1







                print "\n\n"
            print colsize, colwidth
            print sliceNameList
            for item in sliceNameList:
                print list(item)
            #print rowsize, rowwidth




        #print theArray[0:3, 2:3], "0 2 3 3", "\n"
        #print theArray[0:3, 3:5], "0 3 3 5"





        """print "\n", theArray[0:1, 0:int(requirements[1])], \
                                int(np.sum(theArray[0:1, 0:int(requirements[1])]))
                        
                                print "\n", theArray[0:2, 0:3], int(np.sum(theArray[0:2, 0:3]))
                        
                                print "\n", theArray[0:3, 0:2], int(np.sum(theArray[0:3, 0:2])), "\n"
                                """

        #theArray[0:3,1:3]
        # [0:3] means all the rows from 0 to 3. 
        #and [1:3] means all columns from column 1 to column 3

        print " NUMPY ARRAY ITERATION"

        """for irow in reversed(range(int(requirements[2]),  int(requirements[1])+1, 1)):
                                    print theArray[0:1, 0:irow], int(np.sum(theArray[0:1, 0:irow])), "\n" #, \
                                    for icol in range(2*int(requirements[2]), int(requirements[0])):
                                        print theArray[0:icol, 0:irow], int(np.sum(theArray[0:icol, 0:irow])) 
                                    #int(theArray[0:irow, 0:int(requirements[1])])"""

        '''for key, value in factorsDict.iteritems():
                                    #pizzaArray = theArray[0:key, 0:value]
                                    #print pizzaArray
                                    countRow=0
                                    while countRow <= int(requirements[0]):
                                        for irow in reversed(range(key, int(requirements[1])+1, value)):
                                            print theArray[0:key, 0:irow], "\n", theArray[0:irow, 0:key], "\n\n"
                                            countRow+=key'''



        #Rough Work
        #print theArray[0, :] 
        #print theArray[0:0, 0:1]#, theArray[0:1, 2:2], theArray[0:1,1:3], 
        #print theArray[0:1, 2:4] 
        #print theArray[1, :], theArray[2, :]
        #print theArray[:, 0::3]
        #row:requirements[0] colum=requirements[1]
        #print "\n", theArray[0:int(requirements[0]), 0:int(requirements[1])],\
        #int(np.sum(theArray[0:int(requirements[0]), 0:int(requirements[1])]))

        """print theArray[0:3, 0:int(requirements[1])]
        print theArray[0:2, 0:int(requirements[1])]
        print theArray[0:1, 0:int(requirements[1])]"""

        """rectListcount = 0
                                while rectListcount < len(rectList) :
                                    print rectList[rectListcount]
                                    pizzarow = int(rectList[rectListcount])
                                    rectListcount+=1
                                    print rectList[rectListcount]
                                    pizzacol = int(rectList[rectListcount])
                                    pizzaArray = theArray[:pizzarow, :pizzacol]
                                    print pizzaArray
                                    rectListcount+=1"""










filename = 'example.in'
#filename = 'small.in'
#filename = 'medium.in'
googleHash(filename)