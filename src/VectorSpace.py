#!/usr/bin/env python

from numpy import * #http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
import math, random
import InvertedIndex as ii
import WebIndexer as wi

def vectorLength(v):
    return (sum(v**2.0))**0.5

class VectorSpace:
    index = None
    indexer = None
    vectorIndex = None
    numberOfTerms = 0
    numberOfDocs = 0
    
    def __init__(self, iIndex, iIndexer):
        self.index = iIndex
        self.indexer = iIndexer
        self.numberOfTerms = len(self.index)
        self.numberOfDocs = len(self.indexer.docL)
    
    def computeIDF(self, term):
        df = self.index.df(term)
        return math.log( (float(self.numberOfDocs)/df), 10 )

    def buildVectors(self):
        # iterate the index and swap 0 to tfidf where applicable
        #print "swapping 0s for real tfidf..."
        self.vectorIndex = zeros( (self.numberOfDocs, self.numberOfTerms) )
        pos = 0
        for term in self.index: #this gives "ball"
            idf = self.computeIDF(term)
            for entry in self.index[term]: #this gives [ [25, 1], [587, 6], .... ]
                self.vectorIndex[entry[0], pos] = entry[1]*idf
            pos += 1
            
    def length(self, vectorID):
        return vectorLength(self.vectorIndex[vectorID])

    def centroid(self, listOfIDs):
        c = zeros( (self.numberOfTerms) )
        for docId in listOfIDs:
            c = add(c, self.vectorIndex[docId])
        c = c / len(listOfIDs)
        return c

    def distance(self, id1, id2):
        return vectorLength(self.vectorIndex[id1] - self.vectorIndex[id2])

def main():
    index = ii.InvertedIndex()
    indexer = wi.WebIndexer()
    ii.load("../index/fullindex.csv", index)
    vectorSpace = VectorSpace(index, indexer)
    vectorSpace.buildVectors()

    # Length tests
    length(vectorIndex, 1)
    length(vectorIndex, 2)
    length(index, 3)
    length(index, 4)

    # Centroid test
    centroid = findCentroid( index, [1,2,3], numberOfTerms )
    vectorLength(centroid)

    # Dot product
    print vdot(index[100], index[5])

    # Distance
    a1 = array ( [1,2,3,4,5,6,7,8] )
    a2 = array ( [ 0,1,2,3,4,5,6,7] )
    print distance(index, 1, 2)

#main()
