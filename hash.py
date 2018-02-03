filename = 'small.in'
def weatherList(filename):
	with open(filename) as dataset:
        for line in dataset:
            print line
