#!/usr/bin/python

import os.path, sys, getopt, re
import src.InvertedIndex as ii
import src.Tokeniser as tk
import src.WebIndexer as wi
import src.VectorSpace as vs

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    """# Create Index
    index = ii.InvertedIndex()
    indexer = wi.WebIndexer()
    tokeniser = tk.Tokeniser()
    indexer.spimi(index, tokeniser)
    """
    # Load Index
    index = ii.InvertedIndex()
    ii.load("index/fullindex.csv", index)
    indexer = wi.WebIndexer()
    wi.load("index/doclength.csv", indexer.docL)
    
    vSpace = vs.VectorSpace(index, indexer)
    vSpace.buildVectors()
    for i in range(vSpace.numberOfTerms):
        print 0, vSpace.vectorIndex[0, i]
        print 1, vSpace.vectorIndex[1, i]
        print 'c', vSpace.centroid([0,1])[i]

if __name__ == "__main__":
    sys.exit(main())
