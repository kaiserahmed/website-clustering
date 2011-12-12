#!/usr/bin/env python

"""Clustering.py

Implements K-Means clustering on document vectors
"""

import numpy, random
from matplotlib import pyplot as pp

docList = array([])

def rssK(v, u):
    rss = 0.0
    for doc in range(len(v)):
        for d in range(len(doc)):
            rss += (v[d] - docList[d])**2

def rss(w):
    result = 0.0
    for i in range(len(w)):
        result += rssK(w[i])
    return result

def randomSeed(k):
    w = []
    for i in range(k):
        w.append([])
    for n in len(docList):
        w[random.randrange(0,k)].append(n)
    return w

def kMeans(k):
    # Initial seed and centroid
    w = randomSeed(k)
    u = []
    for i in range(k):
        u.append(centroid(w[i]))
    thisRSS = rss(u)
    prevRSS = 0
    while thisRSS != prevRSS:
        for i in range(k):
            w[i] = []
        for n in range(len(docList)):
            distances = [dist(u[i], docList[n]) for i in range(k)]
            j = min(xrange(k), key=distances.__getitem__)
            w[j].append(n)
        for i in range(k):
            u[i] = centroid(w[i])
        prevRSS = thisRSS
        thisRSS = rss(u)
    return u

def kMeansPlot()
    results = []
    tries = []
    for i in range(2, 100)
        kMeans(i)
