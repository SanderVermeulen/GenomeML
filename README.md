# GenomeML
Detecting antimicrobial resistance in assembled genomes by counting k-mers using machine learning. WIP.

# Current features
K-mer counting from fasta files with user defined k-mer size. Additionally, when provided with proper input data (see Usage), able to merge output data from the k-mer counting with resistance information to a machine learning friendly format. A script for training the data on the Random Forest algorithm is also included.

# Usage
Input requires assembled fasta files of the dataset that will be used for training the Random Forest algorithm. In theory raw reads should work, but I suspect the accuracy will suffer if raw reads are used. For the results shown here ABySS (2.3.7) was used with the following settings:

```
abyss-pe j=6 k=35 name=${accession} B=14G in="${file1} ${file2}" -C "${output_folder}/${accession}"
```

The k-mer counting program is usable with the command line.

# Ideas/to-do
At the moment the program only considers non-canonical k-mers. Can change this to support canonical k-mers to see if this improves performance.

# Data source
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6310291/#pcbi.1006258.s010

# References 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8722762/

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10809114/

