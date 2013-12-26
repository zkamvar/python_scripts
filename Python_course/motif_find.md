#### Assignment 3

For this assignment, we're going to use regular expressions to look for a binding-site motif in a set of promoter sequences!

In your class directory, create a program called **<tt>motif_find.py</tt>**. You'll need to import both the <tt>sys</tt>
and <tt>re</tt> packages.

**1.** In this program, create a function called <tt>reverse_complement</tt>, which takes as input a DNA string, and returns the
reverse compliment of the string. You will want to review the topics from Monday and Wednesday, on string and list operations (pages 43 - 52).
In particular, you'll need to replace G's and C's and A's and T's, but _be careful_- if you replace all the C's with G's, then go
to replace all the G's with C's, you'll find that there are no G's left! You'll need an intermediary character to change the C's to, like X. 
Here's some pseudocode that might help you out:

<pre>
function reverse_compliment; parameters - dna sequence as a string
   replace Cs with Xs
   replace Gs with Cs
   replace Xs with Gs
   replace Ts with Xs
   replace As with Ts
   replace Xs with As
   convert the string into a list of bases
   reverse the list
   join the list back into a string (remember "".join(a_list) ?)
   return the joined list
</pre>

**2. ** Also create a function called count_motif that takes two parameters: a regular expression string to search for, and a dna 
sequence to search in. This function should return the number of times the regular expression matches the sequence. (For this,
you could use either the <tt>re.subn()</tt> function which returns the modified string as well as the number of substitutions done, or the
<tt>re.split()</tt> function, which returns a list string pieces, whose length will be 1 larger than the number of matches.)

**3. ** For execution, your program should read lines of sequences like we've been dealing with so far, in particular this file:

<pre>
less -S /raid1/teaching/MCB/MCB599/599_02_SPRING_13/data/grape_promoters.txt
</pre>

Each line in this file contains a gene id, a <strike>tab</strike> space character, and then the 1000bp upstream region of the gene. For each line, your program
should 1) split the line to get the id and the sequence (preferably by using the <tt>re.split()</tt> method), and compute the reverse complement of the sequence, 2) run the <tt>count_motif</tt> function
on the forward sequence and the reverse compliment using <tt>r"[AT]GATA[GA]"</tt> as the motif, and print the id, the forward count, the 
reverse count, the sum of forward and reverse counts, and the motif searched for. So, the output should look something like:

<pre>
cat /raid1/teaching/MCB/MCB599/599_02_SPRING_13/data/grape_promoters.txt | motif_find.py
</pre>
<pre>
GSVIVT01007450001 0  3  3  [AT]GATA[GA]
GSVIVT01007451001 2  0  2  [AT]GATA[GA]
GSVIVT01007452001 4  0  4  [AT]GATA[GA]
GSVIVT01007454001 2  3  5  [AT]GATA[GA]
GSVIVT01007468001 2  1  3  [AT]GATA[GA]
GSVIVT01007471001 0  1  1  [AT]GATA[GA]
GSVIVT01007473001 1  4  5  [AT]GATA[GA]
GSVIVT01007474001 1  4  5  [AT]GATA[GA]
GSVIVT01007477001 2  1  3  [AT]GATA[GA]
GSVIVT01007479001 0  2  2  [AT]GATA[GA]
GSVIVT01007481001 1  2  3  [AT]GATA[GA]
</pre>

<font color="red">Bonus: </font>This motif is described as the "GATA promoter motif" on 
[this](http://arabidopsis.med.ohio-state.edu/AtcisDB/bindingsites.html) page. Since our program is cool in that it reads
from stdin, and prints to stdout in rows and columns, we can make use of the powerful command line utilities to analyze our data.
For example, we can sort the data to discover which sequence has the most motif matches on the forward strand:

<pre>
cat /raid1/teaching/MCB/MCB599/599_02_SPRING_13/data/grape_promoters.txt | motif_find.py | sort -k2,2g
</pre>

If we do this, the last line printed will contain the ID with the most matches. You can then copy and paste this ID into the
[NCBI protein search website](http://www.ncbi.nlm.nih.gov/protein/), to see the full protein sequence of the gene, and from there BLAST it on NCBI to 
figure out its putative function.