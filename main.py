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
    index = ii.InvertedIndex()
    tokeniser = tk.Tokeniser()
    indexer = wi.WebIndexer()
    indexer.spimi(index, tokeniser=tokeniser)
    print indexer.urls
    indexer.display(0)

    matrix = vs.VectorSpace(index, indexer)


if __name__ == "__main__":
    sys.exit(main())
