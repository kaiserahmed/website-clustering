#!/usr/bin/env python

from numpy  import * #http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
import InvertedIndex as ii
import WebIndexer as wi


class VectorSpace:
      index = None
      vectorIndex = None
      indexer = None
      numberOfTerms = None

      ###
      # MAIN
      ###
      def __init__(self, iIndex, iIndexer):
            self.index = iIndex
            self.indexer = iIndexer
            main()
            
      
      ###
      # MATRIX CONSTRUCTION returns( [matrix, number of terms] )
      ###
      def buildVectors(self):
            numberOfTerms = len(self.index)
            docList = zeros( (len(self.indexer.docL), numberOfTerms), dtype=int16 )

            #  n = float(len(self.indexer.docL))
            #  df = self.index.df(term)
            #  return math.log( (n/df), 10 )

            # iterate the index and swap 0 to tfidf where applicable
            print "swapping 0s for real tf..."
            pos = 0 
            for term in self.index: #this gives "ball"
                  for entry in self.index[term]: #this gives [ [25, 1], [587, 6], .... ]
                        docList[entry[0], pos] = entry[1]
                  pos += 1
            return [docList, numberOfTerms]


      ###
      # VECTOR LENGTH returns( int )
      ###
      def length(self, vectorID):
            print "Finding length of document id:", vectorID
            doc = array(self.vectorIndex[vectorID], dtype=int16)
            length = 0            
            for entry in doc:
                  length += entry**2

            length**.5
            print length
            return length


      ###
      # CENTROID LENGTH returns(int)
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
      # FIND CENTROID returns( array )
      ###
      def findCentroid(self, listOfIDs):
            
            centroid = zeros( self.numberOfTerms, dtype=int16)

            for dID in listOfIDs:
                  pos = 0
                  for value in self.vectorIndex[dID]:
                        centroid[pos] += value
                        pos += 1      
            return centroid


      ###
      # VECTOR DISTANCE returns( int )
      ###
      def distance(self, id1, id2):
            a1 = self.vectorIndex[id1]
            a2 = self.vectorIndex[id2]

            length = 0
            pos = 0
            for entry in a1:
                  length +=  (entry - a2[pos])**2
                  pos +=1
                  
            length**.5
            return length


def main():
      index = ii.InvertedIndex()
      indexer = wi.WebIndexer()
      ii.load("fullindex.csv", index)
      vectorSpace = VectorSpace(index, indexer)

      # Initialize
      resultSet                        = vectorSpace.buildVectors()
      self.numberOfTerms      = resultSet[1]
      self.vectorIndex              = resultSet[0]

      # Length tests
      length(self.vectorIndex, 1)
      length(self.vectorIndex, 2)
      length(index, 3)
      length(index, 4)

      # Centroid test
      centroid = findCentroid( index, [1,2,3], numberOfTerms )
      centroidLength(centroid)

      # Dot product
      print vdot(index[100], index[5])

      # Distance
      a1 = array ( [1,2,3,4,5,6,7,8] )
      a2 = array ( [ 0,1,2,3,4,5,6,7] )
      print distance(index, 1, 2)
