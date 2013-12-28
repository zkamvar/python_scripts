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

#==============================================================================#
# Each node in the graph will be a function definition. Functions in R are
# defined as so:
# function_name <- function(args, ...){
# 	## Do something
# }
# The <- and = are interchangeable, so that must be accounted for.
#==============================================================================#
def find_function_def(line):
	arrow = re.findall(r'^\s*[A-Za-z0-9\._]+?\s*\<\-\s*function', line)
	equal = re.findall(r'^\s*[A-Za-z0-9\._]+?\s*=\s*function', line)
	if len(arrow) > 0:
		line = re.split(r'\s*\<\-\s*', arrow[0])[0]
		return line
	elif len(equal) > 0:
		line = re.split(r'\s*=\s*', equal[0])[0]
		return line
	else:
		return False

#==============================================================================#
# The following three functions count open and closed braces. This is important
# for determining when functions end as they can wrap several lines. Escape
# are detected and not counted.
#==============================================================================#
def escaped_braces(line, brace):
	if brace == '{':
		pattern = r'\\\{|\[\{\]'
	elif brace == '(':
		pattern = r'\\\(|\[\(\]'
	elif brace == '}':
		pattern = r'\\\}|\[\}\]'
	elif brace == ')':
		pattern = r'\\\)|\[\)\]'
	escaped = len(re.findall(pattern, line))
	return escaped
def open_braces(line):
	curly = len(re.findall(r'\{', line)) - escaped_braces(line, '{')
	parens = len(re.findall(r'\(', line)) - escaped_braces(line, '(')
	return [curly, parens]
def closed_braces(line):
	curly = len(re.findall(r'\}', line)) - escaped_braces(line, '}')
	parens = len(re.findall(r'\)', line)) - escaped_braces(line, ')')
	return [curly, parens]
def braces_updater(line):
	ob = open_braces(line)
	cb = closed_braces(line)
	return [ob[0] - cb[0], ob[1] - cb[1]]

#==============================================================================#
# Functions in R can be nested within one another:
# eg. vapply(1:10, function(x) mean(cumsum(sample(x, replace = TRUE))), 1)
# This function will attempt to decompose these functional clusters into
# all functions called. The example above contains four functions:
# In the order evaluated: vapply, sample, cumsum, mean
#==============================================================================#
def decompose_nesting(line):
	funk_matches = re.findall(r'([A-Za-z0-9\._]+?)\(', line)
	if len(funk_matches) > 0:
		refined_funk = []
		for funk in funk_matches:
			if funk not in ["function", "if", "for", "while", "return", "cat",\
				"warning", "stop", "stopifnot", "c", "try"]:
				# print("FUNK:\t%s" % funk)
				refined_funk.extend([funk])
		return refined_funk
#==============================================================================#
# Function that will check for apply-type function calls as they have variable
# arguments.
#
# In regex hell. Be back later.
#==============================================================================#
def check_for_apply(line):
	potential_apply = re.findall(r'(\w*apply)', line)
	if potential_apply:
		print(potential_apply)
	funk_call = re.search(r'function', line)
	if funk_call:
		print(funk_call.group())
	args = re.findall(r',\s*(\w+?).*$', line)
	if args:
		print(args)
	if braces_updater(line)[1] == 0 and potential_apply and not funk_call:
		# Do something
		print(line)
	return None

def woot():
	print("woot")


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
			package_directory = os.path.abspath(os.path.expanduser(arg))
		else:
			usage()

	R_directory = "/".join([package_directory, "R"])
	if cfunk:
		src_directory = "/".join([package_directory, "src"])
		for f in os.listdir(src_directory):
			print(f)

	starting_directory = os.getcwd()
	os.chdir(R_directory)

	open_curly_brace = 0
	open_parens = 0
	current_funk = 'unk'

	for f in os.listdir(R_directory):
		#print("\nFile:\t%s %s%s" % (f, "="*(69 - len(f)), ">"))
		if f.endswith(".R") or f.endswith(".r"):
			R_file = io.open(f)
		else:
			continue
		for line in R_file:
			line = line.strip()
			if re.match(r'^\s*#', line) or re.match(r'^\s*$', line):
				continue
			brace_update = braces_updater(line)
			open_curly_brace += brace_update[0]
			open_parens += brace_update[1]
			is_function = find_function_def(line)
			if is_function:
				#print("\n{ (| %s\n- -" % is_function)
				current_funk = is_function
			#print("%d %d| %s" % (open_curly_brace, open_parens, line))
			called_funks = decompose_nesting(line)
			if called_funks:
				for funk in called_funks:
					print("%s\t%s" % (current_funk, funk))
			else:
				continue

	os.chdir(starting_directory)



