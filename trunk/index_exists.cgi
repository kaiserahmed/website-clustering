#!/usr/bin/python

import os.path

def main():
    return os.path.exists("index/fullindex.csv") and os.path.exists("index/doclength.csv") and os.path.exists("index/urls.csv")

"""
def main(argv=None):

if __name__ == "__main__":
    sys.exit(main())

"""
