#!/usr/bin/env python

import WebIndexer as wi
import InvertedIndex as ii
import timeit

# Vector construction
def buildVectors(numberOfDocuments=22000):
    index       = ii.InvertedIndex()
    print "Loading inverted index..."
    ii.load("index/fullindex.csv", index)
    #index: loaded from a file. it's a dictionary that points to a list of lists. example: 
    #       "ball" -> [ [25, 1], [587, 6], .... ]
    #       "toy" -> [ [1, 19], [2073, 2], .... ]
    numberOfTerms = len(index)
    docList = dict()
    filler = []

    # This has the format docID -> [list of 0s]
    print "Building filler docList..."
    for id in xrange(numberOfDocuments):
        docList[id] = []
        for i in xrange(numberOfTerms):
            docList[id].append(0)
    
     # now we have 22000 rows each filled with a list of 27000 '0's

     # iterate the index and swap 0 to tfidf where applicable
    print "swapping 0s for real tfidf..."
    pos = 0 
    for term in index: #this gives "ball"
        for entry in index[term]: #this gives [ [25, 1], [587, 6], .... ]
            (docList[entry[0]])[pos] = entry[1]  # this seems to do things incorrectly
            # I want the above line to replace the '0' in the filler list at 'pos'
        pos += 1

    print docList[5404]

# run it
buildVectors()
