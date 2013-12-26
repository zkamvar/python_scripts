'''
A module for parsing SNP files produced by CLC bio.
By Shawn O'Neil, August 2013
'''

import sys
import re

class SNP:
	"""
	A Class representiong a SNP.
	holds:
		alleles
		counts
		reference position
		reference allele
	can tell you:
		transition
		transversion
	"""
	def __init__(self, refal, refpos, refchr):
		self.ref_allele = refal
		self.ref_pos = refpos
		self.ref_chr = refchr
		self.allele_counts = dict()
	def add_allele_count(self, allele, count):
		"""
		Add count to the allele, even if already present.
		"""
		if(self.allele_counts.has_key(allele)):
			self.allele_counts[allele] = self.allele_counts[allele] + count
		else:
			self.allele_counts[allele] = count

	def get_coverage(self):
		"""
		Count the number of fragments containing the SNP.
		"""
		sum = 0
		counts = self.allele_counts.values()
		for count in counts:
			sum = sum + count
		return(sum)

	def is_transversion(self):
		"""
		Returns 'True' if the SNP represents a transversion. Otherwise, 'False' 
		"""
		alleles = self.allele_counts.keys()
		if(alleles[0] == "A" or alleles[0] == "G"):
			if(alleles[1] == "C" or alleles[1] == "T"):
				return(True)
		elif(alleles[0] == "C" or alleles[0] == "T"):
			if(alleles[1] == "A" or alleles[1] == "G"):
				return(True)
		return(False)	

	def is_transition(self):
		"""
		Returns 'True' if the SNP represents a transition. Otherwise, 'False'
		"""
		is_transversion = self.is_transversion()
		return(not(is_transversion))


class Chromosome:
	"""
	Chromosome class- holds a dictionary of reference positions to SNPs.
	"""
	def __init__(self, nameparam):
		self.name = nameparam
		self.pos_to_snps = dict()
	
	def add_snp(self, pos, snp):
		if(self.pos_to_snps.has_key(pos)):
			print("Whoops! We've already got a snp at pos " + str(pos))
		else:
			self.pos_to_snps[pos] = snp

	def count_transitions_over_coverage(self, cutoff):
		positions = self.pos_to_snps.keys()
		count = 0
		for position in positions:
			snp = self.pos_to_snps[position]
			if(snp.is_transition() and snp.get_coverage() > cutoff):
				count = count + 1
		return(count)

	def count_transversions_over_coverage(self, cutoff):
		positions = self.pos_to_snps.keys()
		count = 0
		for position in positions:
			snp = self.pos_to_snps[position]
			if(snp.is_transversion() and snp.get_coverage() > cutoff):
				count = count + 1
		return(count)

def clcsnps_to_chr_dict(fhandle):
	chr_dict = dict()
	header_line = fhandle.readline()

	for line in fhandle:
		line_stripped = line.strip()
		line_list = line.split(',')
		chr_name = line_list[0]
		ref_pos = int(line_list[1])
		ref_allele = line_list[5]
		var1 = line_list[8]
		var1_count = int(line_list[10])
		var2 = line_list[11]
		var2_count = int(line_list[13])
		
		newsnp = SNP(ref_allele, ref_pos, chr_name)
		newsnp.add_allele_count(var1, var1_count)
		newsnp.add_allele_count(var2, var2_count)

		if(chr_dict.has_key(chr_name)):
			chromo = chr_dict[chr_name]
			chromo.add_snp(ref_pos, newsnp)
		else:
			chromo = Chromosome(chr_name)
			chromo.add_snp(ref_pos, newsnp)
			chr_dict[chr_name] = chromo
	fhandle.close()
	return(chr_dict)


