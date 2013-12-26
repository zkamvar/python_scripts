#!/usr/bin/env python2.7

import io, re, getopt

'''
This script will scrape all function calls from an R package and create a matrix
that can be used with the igraph R package to plot a graph of all the functions.

Yes, igraph is available for python, but I am not as familiar with it. 
'''