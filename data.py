#!/usr/bin/python

import sys, os, csv
import src.InvertedIndex as ii
import src.WebIndexer as wi
import src.VectorSpace as vs

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    index = ii.InvertedIndex()
    ii.load("index/fullindex.csv", index)
    indexer = wi.WebIndexer()
    indexer.load()
    
    vSpace = vs.VectorSpace(index, indexer)
    vSpace.buildVectors()

    minK = 2
    maxK = 10
    n = 1

    results = []
    if not os.path.exists("index/kmeans.csv"):
        for k in range(minK, maxK+1):
            print k
            w, u, rss = vSpace.kMeansBestOfN(k, n)
            results.append(rss)
        w=csv.writer(file(r'index/kmeans.csv','wb'))
        w.writerows(results)
    else:
        reader = csv.reader(open("index/kmeans.csv", "rb"))
        for row in reader:
            print row[0]

if __name__ == "__main__":
    sys.exit(main())
