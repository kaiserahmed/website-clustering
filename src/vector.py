#!/usr/bin/env python

from numpy  import * #http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
import InvertedIndex as ii

###
# MATRIX CONSTRUCTION ( [matrix, number of terms] )
###
def buildVectors(numberOfDocuments=22000):
    index       = ii.InvertedIndex()
    print "Loading inverted index..."
    ii.load("fullindex.csv", index)

    numberOfTerms = len(index)
    docList = zeros( (numberOfDocuments, numberOfTerms), dtype=int16 )

    # iterate the index and swap 0 to tfidf where applicable
    print "swapping 0s for real tfidf..."
    pos = 0 
    for term in index: #this gives "ball"
        for entry in index[term]: #this gives [ [25, 1], [587, 6], .... ]
            docList[entry[0], pos] = entry[1]
        pos += 1
    return [docList, numberOfTerms]


###
# VECTOR LENGTH ( int )
###
def length(index, vectorID):
      print "Finding length of document id:", vectorID
      doc = array(index[vectorID], dtype=int16)
      length = 0            
      for entry in doc:
            length += entry**2

      length**.5
      print length
      return length


###
# CENTROID LENGTH (int)
###
def centroidLength(centroid):
      print "Finding length of centroid"

      length = 0            
      for entry in centroid:
            length += entry**2

      length**.5
      print length
      return length

###
# FIND CENTROID ( array )
###
def findCentroid(index, listOfIDs, numberOfTerms):
      
      centroid = zeros( numberOfTerms, dtype=int16)

      for dID in listOfIDs:
            pos = 0
            for value in index[dID]:
                  centroid[pos] += value
                  pos += 1      
      print centroid
      return centroid
      
      
###
# MAIN
###

# Declare constants
numberOfDocuments=22000

# Initialize
resultSet                  = buildVectors( numberOfDocuments )
numberOfTerms      = resultSet[1]
index                      = resultSet[0]

# Length tests
length(index, 1)
length(index, 2)
length(index, 3)
length(index, 4)

# Centroid test
centroid = findCentroid( index, [1,2,3], numberOfTerms )
centroidLength(centroid)
