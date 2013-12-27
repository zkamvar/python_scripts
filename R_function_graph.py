#!/usr/bin/env python2.7

import io, sys, re, getopt, os

'''
This script will scrape all function calls from an R package and create a matrix
that can be used with the igraph R package to plot a graph of all the functions.

Yes, igraph is available for python, but I am not as familiar with it. 
'''

def usage():
	print("\n%s Copyright (C) Zhian N. Kamvar 2013" % sys.argv[0])
	print("Software comes with no warranty.")
	print("Usage:\n\tpython %s -d <path/to/R-package>")
	print("Options:")
	print("\t-h:\tShow help and quit.")
	print("\t-v:\tVerbose.")
	print("\t-c:\ttraverse /src directory for C functions")
	print("")
	sys.exit(2)



if __name__ == '__main__':

	verbose = False
	cfunk = False
	package_directory = ""
	myopts, args = getopt.getopt(sys.argv[1:], "hvcd:", ["directory="])

	if len(myopts) < 1:
		usage()

	for opt, arg in myopts:
		if opt == "-h":
			usage()
		elif opt == "-v":
			verbose = True
		elif opt == "-c":
			cfunk = True
		elif opt in ("-d", "--directory"):
			package_directory = os.path.abspath(arg)
		else:
			usage()

	R_directory = "/".join([package_directory, "R"])
	if cfunk:
		src_directory = "/".join([package_directory, "src"])
		for f in os.listdir(src_directory):
			print(f)

	print("Verbose: "+str(verbose))
	print("C Funk: "+str(cfunk))
	print("R Package Directory: "+ package_directory)

	for f in os.listdir(R_directory):
		print(f)


	



