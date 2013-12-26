#!/usr/bin/env python2.7

import sys

if(sys.stdin.isatty()):
	print("usage: cat <file> | ./go_counts.py")
	quit()	

terms_to_gocounts = dict()
for line in sys.stdin:
	line_stripped = line.strip()
	line_list = line_stripped.split("\t")
	gid = line_list[0]
	gonum = line_list[1]
	term = line_list[2]
	if(terms_to_gocounts.has_key(term)):
		subdict = terms_to_gocounts[term]
		if(subdict.has_key(gonum)):
			subdict[gonum] += 1
		else:
			subdict[gonum] = 1
	else:
		subdict = dict()
		subdict[gonum] = 1
		terms_to_gocounts[term] = subdict

terms = terms_to_gocounts.keys()
for term in terms:
	subdict = terms_to_gocounts[term]
	gonums_sublist = subdict.keys()
	for gonum in gonums_sublist:
		count = subdict[gonum]
		print(term + "\t" + gonum + "\t" + str(count))

