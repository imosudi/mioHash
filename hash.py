filename = 'example.in'
#filename = 'small.in'
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
        for line in dataset:
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
        print ' %s numbers of \'M\' \n %s numbers of \'T\' ' % (countM, countT)







googleHash(filename)
