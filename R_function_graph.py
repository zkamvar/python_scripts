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

def find_function_def(line):
	line = re.findall(r'\s*[A-Za-z0-9\._]+?\s*\<\-\s*function', line)
	if len(line) > 0:
		line = re.split(r'\s*\<\-\s*', line[0])[0]
		return line
	else:
		return False

def open_braces(line):
	curly = len(re.findall(r'\{', line)) - len(re.findall(r'\}', line))
	parens = len(re.findall(r'\(', line)) - len(re.findall(r'\)', line))
	return [curly, parens]


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

	# print("Verbose: "+str(verbose))
	# print("C Funk: "+str(cfunk))
	# print("R Package Directory: "+ package_directory)

	os.chdir(R_directory)

	open_curly_brace = 0
	open_parens = 0

	for f in os.listdir(R_directory):
		print("\nFile:\t%s %s%s" % (f, "="*(69 - len(f)), ">"))
		if f.endswith(".R") or f.endswith(".r"):
			R_file = io.open(f)
		else:
			continue
		for line in R_file:
			line = line.strip()
			if re.match(r'^\s*#', line) or re.match(r'^\s*$', line):
				continue
			brace_update = open_braces(line)
			open_curly_brace += brace_update[0]
			open_parens += brace_update[1]
			is_function = find_function_def(line)
			if is_function:
				print("\n{ (| %s\n- -" % is_function)
			# open_curly_brace -= len(re.findall(r'\}', line))
			# open_parens -= len(re.findall(r'\)', line))
			print("%d %d| %s" % (open_curly_brace, open_parens, line))

	



