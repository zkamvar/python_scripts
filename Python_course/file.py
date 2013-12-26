#!/usr/bin/env python2.7
import io
import math

fhandle = io.open("blast.txt")
count = 0
sum = 0.0
evals = list()

for line in fhandle:
	eval = float(line.split("\t")[10])
	sum = sum + eval
	count = count + 1
	evals.append(eval)

fhandle.close()
mean = sum/count
ss_diff = 0.0

for eval in evals:
	ss_diff = ss_diff + (mean - eval)**2

ratio = ss_diff/(count - 1)
sqrtval = math.sqrt(ratio)
print("Total nubmer of e-values: "+str(count)+"\n\tMean:\t"+str(mean)+"\n\tStandard Deviation:\t"+str(sqrtval)+"\n\tVariance:\t"+str(ratio))


