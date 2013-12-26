#### Assignment 6

This assignment will be extension of our class example, that provides significant functionality to our "chromosome" class with fairly minimal (though
somewhat tricky) coding.

First, you should implement the code we discussed in class (see the notes, pages 86-93), and test it out with:
<pre> 
cat /raid1/teaching/data/python/SNP_Analysis2.cvs | ./snp_count.py
</pre>

Next, you should add a method to the Chromosome class called <tt>**print_stats_on_snps_window**</tt>, which will
take one parameter (aside from self): a list containing integers called <tt>snp_positions</tt>, which contain keys you can assume are in the <tt>self.pos_to_snps</tt>
dictionary. Given this list, you should compute three things: 1) the percentage of SNPs at those positions that are transitions
, 2) the averave of the numbers in <tt>snp_positions</tt> (the "average position" of the set--you may want to create a helper method you can 
call to return the mean of a list of numbers), and 3) the number of snps per 1000 base pairs as represented in the position. This is defined as
the number of SNPs defined by the position list (<tt>len(snp_positions)</tt>)*1000, divided by the size of the chromosomal window the SNPs cover
(note that Python has built-in <tt>min()</tt> and <tt>max()</tt>, so the range is simply <tt>min(snp_positions) - max(snp_positions) + 1</tt>).
With these three values in hand, have the method print them along with the chromosome name, like so:
<pre>
      print(self.name + "\t" + str(mean_pos) + "\t" + str(snps_per1000bp) + "\t" + str(trans_rate))
</pre>

Next, we'll do something analygous to our earlier exercise of computing a sliding-window GC content. Add a method to 
the <tt>Chromosome</tt> class called <tt>**print_stats_per_window**</tt>, that does the following things: 1) extracts all the
snp positions from <tt>self.pos_to_snps.keys()</tt>, 2) creates a sorted version of this list using the <tt>sorted()</tt> function
called <tt>sorted_positions</tt>, 
3) uses a for-loop to extract sub-lists of this using a 100-snp window, starting from sorted_positions[0:0+100] to the last window. 
(Don't forget to draw a quick picture to figure out what the last index in the for loop/range() call is--I had to!), and then
calls the <tt>self.print_stats_on_snps_window</tt> on each window.

Finally, in the end of the program, rather than calling the <tt>count_transitions_over_coverage</tt> and <tt>count_transversions_over_coverage</tt>
methods and printing the results for each chromosome, simply call each chromosomes <tt>print_stats_per_window</tt> method.

**<font color="red">Super Cool Bonus</font>**
Now, given this output we can produce some amazing plots, but we'll use a quick R-script and ggplot 2 to do so. That means that you'll first need to
fire up R and install the ggplot2 library by running the following:

<pre>
R
....
> install.packages("ggplot2")
....(follow instructions, say "yes" if asked questions)
....
>quit(save = "no")
</pre>

Now we can run the script in combination with a couple of complex Rscript one-liners, to produce plots called <tt>trans_rate.png</tt> and <tt>snpsper1000bp.png</tt>:

<pre>
cat /raid1/teaching/data/python/SNP_Analysis2.cvs | ./snp_count.py | Rscript -e 'library(ggplot2); data <- read.table("stdin", header = F, col.names = c("Chr", "pos", "snpsper1000bp", "trans_rate"), sep = "\\t"); ggplot(data) + geom_line(mapping = aes(x = pos, y = trans_rate)) + facet_grid(Chr ~ .); ggsave("trans_rate.png")'
cat /raid1/teaching/data/python/SNP_Analysis2.cvs | ./snp_count.py | Rscript -e 'library(ggplot2); data <- read.table("stdin", header = F, col.names = c("Chr", "pos", "snpsper1000bp", "trans_rate"), sep = "\\t"); ggplot(data) + geom_line(mapping = aes(x = pos, y = snpsper1000bp)) + facet_grid(Chr ~ .); ggsave("snpsper1000bp.png")'
</pre>
</p>

Now: here's a question we might ask about these results: are they really a "sliding window" analysis over the Chromosome? If not, do you think they are 
more, or less, representative of these statistics at each chromosomal location? Can you think of a way to do a fixed-width sliding window approach?