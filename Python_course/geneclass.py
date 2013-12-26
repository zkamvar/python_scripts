#!/usr/bin/env python2.7

class Gene:
	def __init__(self, creationid):
		print("\nI'm a new gene object!")
		print("My constructor got a param: " + creationid)
		print("Assigning that param to my id")
		self.id = creationid
		print("Assigning an empty string to my seq")
		self.seq = ""

	def print_id(self):
		print("\n=========\nMy id is: " + self.id)

	def compute_gc(self):
		g_count = self.seq.count("G")
		c_count = self.seq.count("C")
		gc = float(g_count + c_count)/len(self.seq)
		return(gc)
	
	def set_seq(self, sequenceparam):
		print("\nSetting my sequence to the param!")
		self.seq = sequenceparam

geneA = Gene("CYP6B")
geneB = Gene("CATB")
geneA.print_id()
geneB.print_id()
geneA.set_seq("ACTGACTTGA")
gc_A = geneA.compute_gc()
print(str(gc_A))
