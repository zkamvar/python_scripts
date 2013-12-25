#!/usr/bin/env python2.7

import os, sys, getopt
path = ""
pattern = "this is not a pattern we should see"
word = "this is not a word we should see"
replacement = ""
counter = 0


def usage():
	print("")
	print("Usage: python %s -d path/to/dir -p <pattern> -w <word> -r <replacement>" % sys.argv[0])
	print("")
	sys.exit(2)

myopts, args = getopt.getopt(sys.argv[1:], "d:p:w:r:", ["dir=", "pattern=", "word=", "replacement="])

if len(myopts) < 4:
	usage()


print(myopts)

for opt, arg in myopts:
	if opt in ("-d", "--dir"):
		path = arg
		print(arg)
	elif opt in ("-p", "--pattern"):
		pattern = arg
		print(arg)
	elif opt in ("-w", "--word"):
		word = arg
		print(arg)
	elif opt in ("-r", "--replacement"):
		replacement = arg
		print(arg)
	else:
		usage()
'''
for i in sorted(os.listdir(path)):
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
		os.rename(i, res)
	else:
		print("Just us chickens!")
'''
	


