#!/usr/bin/env python2.7

import io 

dna = io.open("/raid1/teaching/data/python/lines_seqs.txt")

## given a dna string, returns gc content (0-1)
def compute_gc_content(seq):
    g_cont = base_composition(seq, "G")
    c_cont = base_composition(seq, "C")
    gc_cont = g_cont + c_cont
    return(gc_cont)

## given a string seq, and a single char string base,
## returns the percentage of seq compased of "base"
def base_composition(seq, base):
    base_counter = 0
    seq_len = len(seq)
    # index will range from 0 to seq_len-1, which are the first
    # and last indices in the string
    for index in range(0,seq_len):
        seq_base = seq[index]
        if(seq_base == base):
            base_counter = base_counter + 1
    
    base_percent = float(base_counter)/float(seq_len)
    return(base_percent)

def gc_window(id, seq):
	sum = 0.0
	count = 0
	window_size = 5
	win_len = len(seq) - window_size + 1 
	for windex in range(0, win_len):
		gc = compute_gc_content(seq[windex:windex+window_size])
		sum += gc
		count += 1
		#print(id + "\t" + str(windex) + "\t" + str(gc))
	mean = sum/count
	print(id + "\tmean\t" + str(mean))

# Let's create a list of dna sequences
seqs_list = list()
seqs_list.append("ACGA")
seqs_list.append("ACCG")
seqs_list.append("CCGC")
# and print the GC content of each
for seq in seqs_list:
    seq_gc = compute_gc_content(seq)
    print(str(seq_gc) + " : " + seq)
print("===")
gc_window("CYP6B", "ACTAGTACGG")
print("===\nNow for the fun stuff")

for seq in dna:
	seq_list = seq.split("\t")
	id = seq_list[0]
	sequence = seq_list[1]
	seq_gc = compute_gc_content(sequence)
	print("===\t===\t===")
	print(id + "\tobserved gc:\t" + str(seq_gc))
	gc_window(id, sequence)
print("===\t===\t===\n")


