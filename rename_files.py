#!/usr/bin/env python2.7

import os, sys, getopt, re

def usage():
	print("\n%s Copyright (C) Zhian N. Kamvar 2013" % sys.argv[0])
	print("Software comes with no warranty.")
	print("Usage:\n\tpython %s -d path/to/dir -w <word> -r <replacement>" % sys.argv[0])
	print("Optional:")
	print("\t-v = verbose")
	print("\t-t = test regex, but don't change anything (implies -v)") 
	print("\t-h = help and quit")
	print("")
	sys.exit(2)

def show_files(files):
	for i in files:
		print(i)

def replace_with_regex(files, word, replacement):
	# show_files(files)
	for i in files:
		matchsticks = re.search(r'%s' % word, i)
		if matchsticks:
			oldstring = i
			newstring = re.sub(r'%s' % word, r'%s' % replacement, i)
			if verbose:
				print("Old: %s\tNew: %s" % (oldstring, newstring))
			if not test:
				os.rename(oldstring, newstring)
		else:
			if verbose:
				print("Unchanged: %s" % i)

'''
	split_and_replace:
	A function to replace a single word in a string separated by a given
	pattern. 

	example iteration:
		this_is_a_file.txt 
		['this', 'is', 'a', 'file.txt'] 
		['this', 'is', 'a', 'file', 'txt']  
		['this', 'was', 'a', 'file', 'txt'] 
		['this_was_a_file', 'txt']
		this_was_a_file.txt

def split_and_replace(files, path, pattern, word, replacement):
	counter = 0
	for i in files:
		curr_count = counter
		splitsville = i.split(pattern)
		splitlen = len(splitsville)-1
		lastone = splitsville[splitlen]
		del splitsville[splitlen]
		splitsville.extend(lastone.split("."))
		for j in range(0, len(splitsville)):
			if splitsville[j] == word:
				splitsville[j] = replacement
				counter += 1
		if curr_count < counter:
			base = "_".join(splitsville[0:len(splitsville)-1])
			res = ".".join([base, splitsville[len(splitsville)-1]])
			print("key: " + i + "\tvalue: " + res)
			frompath = "/".join([path, i])
			topath = "/".join([path, res])
			os.rename(frompath, topath)
			# print("From " + frompath + "\tTo: " + topath)
		else:
			print("Just us chickens!")
'''

if __name__ == '__main__':

	path = ""
	pattern = "this is not a pattern we should see"
	word = "this is not a word we should see"
	replacement = ""
	verbose = False
	test = False

	myopts, args = getopt.getopt(sys.argv[1:], "hvtd:w:r:", ["dir=", "word=", "replacement="])

	if len(myopts) < 3:
		usage()

	# print(myopts)

	for opt, arg in myopts:
		if opt == "-h":
			usage()
		elif opt == "-v":
			verbose = True
		elif opt == "-t":
			test = True
			verbose = True
		elif opt in ("-d", "--dir"):
			path = arg
			# print(arg)
		elif opt in ("-w", "--word"):
			word = arg
			# print(arg)
		elif opt in ("-r", "--replacement"):
			replacement = arg
			# print(arg)
		else:
			usage()


	old_dir = os.getcwd()
	files = sorted(os.listdir(path))

	os.chdir(path)
	if verbose:
		print("Changing to directory %s" % os.getcwd())

	replace_with_regex(files, word, replacement)

	os.chdir(old_dir)
	if verbose:
		print("Changing back to current directory %s" % os.getcwd())
	# split_and_replace(files, path, pattern, word, replacement)



