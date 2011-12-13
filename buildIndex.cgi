#!/usr/bin/python

import os.path, sys, getopt, re
import src.InvertedIndex as ii
import src.Tokeniser as tk
import src.WebIndexer as wi
import src.VectorSpace as vs
import src.SpellingCorrector as sc

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    index = ii.InvertedIndex()
    indexer = wi.WebIndexer()
    tokeniser = tk.Tokeniser()
    indexer.spimi(index, tokeniser)

    vSpace = vs.VectorSpace(index, indexer)
    vSpace.buildVectors()
    
    k = 3
    w, u, rss = vSpace.kMeans(k)

if __name__ == "__main__":
    sys.exit(main())
