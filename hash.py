filename = 'small.in'
def googleHash(filename):
    with open(filename) as dataset:
        for line in dataset:
            print line


googleHash(filename)
