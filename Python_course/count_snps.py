#!/usr/bin/env python2.7

import MySNPModule
import sys

if(sys.stdin.isatty()):
	print("Usage: cat <clcsnps.txt> | ./count_snps.py")
	quit()

chr_dict = MySNPModule.clcsnps_to_chr_dict(sys.stdin)

print("Chromosome \tTs\tTv")
print("==========\t===\t===")
for chr_name in chr_dict.keys():
	chromo = chr_dict[chr_name]
	trs_count = chromo.count_transitions_over_coverage(6)
	trv_count = chromo.count_transversions_over_coverage(6)
	print(chr_name + "\t" + str(trs_count) + "\t" + str(trv_count))
