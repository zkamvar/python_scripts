#!/usr/bin/env python2.7

seq = "ACTAGATACTACAG"

gc_counter = 0

seq_len = len(seq)

for index in range(0, seq_len):
	seq_base = seq[index]
	if(seq_base == "C" or seq_base == "G"):
		gc_counter = gc_counter + 1

gc_content = float(gc_counter)/float(seq_len)
print("gc content is " + str(gc_content))
