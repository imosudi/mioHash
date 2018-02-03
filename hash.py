filename = 'small.in'
def googleHash(filename):
    with open(filename) as dataset:
        #Manipulating the first line from the dataset
        first_line = dataset.readline()
        print first_line

        #Then, the remaining lines
        for line in dataset:
            print line





googleHash(filename)
