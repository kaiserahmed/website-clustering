#!/usr/bin/python


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    numberOfResults = 10
    userInput = "Keywords"

    # Sample: Tokenise input
    terms = tokeniser.tokenise(userInput)

    # Sample: Edit distance
    terms = [sc.correct(term) for term in terms]

    # Sample: Query using cosine-cluster
    queryVector = vSpace.buildQueryVector(terms)
    closestCluster = vSpace.nearestCluster(w, u, queryVector)
    docList = vSpace.cosineSort(range(len(vSpace.vectorIndex)), closestCluster, queryVector)[:numberOfResults]



import sys

    print '{\n'
    for i in range(len(urlList))
        sys.stdout.write('\t"'+str(i+1)+'" : "'+urlList[i]+'"')
        if i != (len(urlList)-1):
            print ','
    print '\n}'


    sys.stdout.write('{\n\t"' + output + '"\n}')
    if 

if __name__ == "__main__":
    sys.exit(main())
