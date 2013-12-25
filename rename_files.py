#!/usr/bin/env python2.7

import os, sys, getopt, re
path = ""
pattern = "this is not a pattern we should see"
word = "this is not a word we should see"
replacement = ""


def usage():
	print("\n%s Copyright (C) Zhian N. Kamvar 2013" % sys.argv[0])
	print("Software comes with no warranty.")
	print("Usage: python %s -d path/to/dir -p <pattern> -w <word> -r <replacement>" % sys.argv[0])
	print("")
	sys.exit(2)

myopts, args = getopt.getopt(sys.argv[1:], "hd:p:w:r:", ["dir=", "pattern=", "word=", "replacement="])

if len(myopts) < 4:
	usage()


# print(myopts)

for opt, arg in myopts:
	if opt == "-h":
		usage()
	elif opt in ("-d", "--dir"):
		path = arg
		# print(arg)
	elif opt in ("-p", "--pattern"):
		pattern = arg
		# print(arg)
	elif opt in ("-w", "--word"):
		word = arg
		# print(arg)
	elif opt in ("-r", "--replacement"):
		replacement = arg
		# print(arg)
	else:
		usage()

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
'''
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

def show_files(files):
	for i in files:
		print(i)

def replace_with_regex(files, word, replacement):
	# show_files(files)
	for i in files:
		print(i + "\t" + str(re.match(re.escape(word), i)))

files = sorted(os.listdir(path))
replace_with_regex(files, word, replacement)
# split_and_replace(files, path, pattern, word, replacement)



