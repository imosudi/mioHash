import numpy as np
from numpy import array

#filename = 'example.in'
filename = 'small.in'
#filename = 'medium.in'

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
        mynumarray = np.random.randn(int(requirements[0]),int(requirements[1]))
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
            print lineList
            for i in range (int(requirements[1])):
                if lineList[i] == "T" :
                    lineList[i] = 0
                if lineList[i] == "M" :
                    lineList[i] = 1
            #lineList = np.array(lineList, dtype=str)
            #print lineList
            #lineList = lineList.astype(np.float)
            mynumarray[rowcount] = np.array(lineList, dtype=str)
            #array2 =np.insert(mynumarray, lineList, axis=count)
            #mynumarray[0] = np.array(lineList)

            #data_array = array( lineList )
            #print data_array
            rowcount+=1
        print mynumarray
        #print mynum

        print ' %s numbers of \'M\' \n %s numbers of \'T\' ' % (countM, countT)

        #data_array2 = np.loadtxt(filename, dtype=str, skiprows=1)
        #print data_array2
        #data = np.loadtxt(filename, delimiter="\n", skiprows=1)









googleHash(filename)
