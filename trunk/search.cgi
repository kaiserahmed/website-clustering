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

    urlList = [indexer.urls[docId] for docId in docList]
    output = ', \n\t'.join(url for url in urlList)

    print """
    {
    \t"""
    print output
    print """
    }
    """

if __name__ == "__main__":
    sys.exit(main())
