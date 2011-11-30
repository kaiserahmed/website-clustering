#!/usr/bin/env python

"""OkapiRanking.py

Given an inverted index and an indexer, will perform ranked retrieval based on
a query by computing the Okapi BM25 ranking of the list of documents indexed.

Marc-Andre Faucher (9614729)
ma.faucher@gmail.com
"""

import csv, math
import InvertedIndex as ii
import ReuterIndexer as ri

class OkapiRanking:
    index   = None
    indexer = None

    def __init__(self, iIndex, rIndexer):
        """ OkapiRanking 
        Assumes both iIndex and rIndexer are populated
        respectively with an index (index) and doc length information (docL)
        """
        self.index = iIndex
        self.indexer = rIndexer

    def idf(self, term):
        n = float(len(self.indexer.docL))
        df = self.index.df(term)
        return math.log( (n/df), 10 )

    def rsv(self, terms, k=1.2, b=0.75, n=10):
        """
        Return a sorted docId list based on the terms
        """
        k = float(k)
        b = float(b)
        results = {}
        lavg = float(self.indexer.avgL())               # Calculate average doc length
        for doc in self.indexer.docL:
            ldoc = float(self.indexer.docL[doc])        # Get doc length
            docrsv = 0.0
            for term in terms:                          # Calculate corresponding rsv
                tf = float(self.index.tf(term, doc))
                docrsv += self.idf(term) * ( ( (k+1.0)*tf ) / ( k*((1.0-b)+b*(ldoc/lavg)) + tf ) )
            results[docrsv] = doc
        # Return list of document ID sorted by decreasing RSV value
        
        documents = [value for key, value, in sorted(results.iteritems(), reverse=True)]
        return [documents[i] for i in range(n)]
