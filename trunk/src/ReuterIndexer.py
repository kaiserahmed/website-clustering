#!/usr/bin/env python

"""ReuterIndexer.py

Parses and indexes a folder of *.sgm files using SPIMI algorithm

Marc-Andre Faucher (9614729)
ma.faucher@gmail.com
"""

import re, glob, csv
import Tokeniser as tk
import InvertedIndex as ii

# I/O

def save(savefile, docList):
    """ Saves the document length information as a CSV
    Inspired by: http://www.doughellmann.com/PyMOTW/csv/#using-field-names
    """
    try:
        f = open(savefile, 'wb')
        fields = ('docId', 'docLength')
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(dict((n,n) for n in fields))
        for key in docList:
            writer.writerow( { fields[0]:key, fields[1]:docList[key] } )
    finally:
        f.close()
 
def load(loadfile, docList):
    """ loads the document length information from a CSV
    Inspired by: http://www.doughellmann.com/PyMOTW/csv/#using-field-names
    """
    docList.clear()
    try:
        f = open(loadfile, 'rb')
        reader = csv.DictReader(f)
        for row in reader:
            docList[int(row['docId'])] = int(row['docLength'])
    finally:
        f.close()

class ReuterIndexer:
    block = 0           # Block size in number of files for SPIMI
    fileList = []       # List of sgm files to index
    docL = {}           # List of doc ID and length

    def __init__(self, folder='reuters21578', blockSize=2):
        """ ReuterIndexer
        folder:     Folder of *.sgm files to parse
        blockSize:  Specify a block size for SPIMI in number of files
        """
        if blockSize > 1:
            self.block = blockSize
        else:
            self.block = 1

        self.fileList = glob.glob(folder+"/*.sgm")
        self.fileList.sort()

    def avgL(self):
        l = 0
        for docId in self.docL:
            l += self.docL[docId]
        return float(l) / float( len(self.docL) )

    def parse(self, doc, index, tokeniser):
        """ Parse a single file and add to InvertedIndex """
        try:
            f = open(doc, 'rb')
            regexId   = re.compile(r'(?<=NEWID=").*?(?=")')
            regexText = re.compile(r'(?<=<REUTERS).*?(?=</REUTERS>)', flags=re.DOTALL)
            regexBody = re.compile(r'(?<=<BODY>).*?(?=</BODY>)', flags=re.DOTALL)
            text = f.read()
            # Find all docId-Article pair
            for (newid, article) in zip(regexId.findall(text), regexText.findall(text)):
                article = regexBody.findall(article)
                if article: # In case there is no body for this docId
                    docId = int(newid)
                    terms = tokeniser.tokenise(article[0])
                    # Record length of document
                    self.docL[docId] = len(terms)
                    # Add terms to inverted index
                    for term in terms:
                        index[term] = int(docId)
        finally:
            f.close()
    
    def spimi(self, index, tokeniser=None):
        """ Implements SPIMI index construction algorithm """
        if tokeniser is None:
            tokeniser = tk.Tokeniser()
        numberofblocks = ( len(self.fileList) + self.block - 1 ) // self.block
        if numberofblocks < 1:
            numberofblocks = 1
        for n in range( numberofblocks ):
            index.clear()
            print "Parsing Block " + str(n) + "... "
            for doc in self.fileList[n*self.block: (n * self.block) + self.block]:
                self.parse(doc, index, tokeniser)
            ii.save("index/index"+str(n)+".csv", index)
        print "Merging... "
        ii.mergeFile( "index/fullindex.csv", [ "index/index"+str(n)+".csv" for n in range(numberofblocks) ] )
        save('index/doclength.csv', self.docL)

    def display(self, docId, folder='reuters21578'):
        try:
            f = open(folder+"/reut2-%(number)03d.sgm" %{ "number" : (docId-1)//1000 })
            text = f.read()
        
            regexText  = re.compile(r'(?<=NEWID="'+str(docId)+').*?(?=</TEXT>)', flags=re.DOTALL)
            regexTitle = re.compile(r'(?<=<TITLE>).*?(?=</TITLE>)')
            regexDate  = re.compile(r'(?<=<DATELINE>).*?(?=</DATELINE>)')
            regexBody  = re.compile(r'(?<=<BODY>).*?(?=&#3;)', flags=re.DOTALL)

            text = regexText.findall(text)[0]
            title=regexTitle.findall(text)[0]
            date = regexDate.findall(text)[0]
            body = regexBody.findall(text)[0]

            print title
            print date.lstrip(), body
        finally:
            f.close()
