# GenomeML
Detecting antimicrobial resistance in assembled genomes by counting k-mers using machine learning

# Current features
K-mer counting from fasta files with user defined k-mer size

# Ideas/to-do
Implement loop over all assembled genomes to save k-mer csv files
Merge individual csv files to one file to feed into random forest classifier:

	K-mer1	K-mer2	K-mer3	Resistant
Sample1 100	321	32	0
Sample2 83	72	831	0
Sample3 93	732	632	1

Implement command line functions k-mer counting script

# Data source
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6310291/#pcbi.1006258.s010

# References 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8722762/
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10809114/

