# GenomeML
Detecting antimicrobial resistance in assembled genomes by counting k-mers using machine learning. Work in progress.

# Current features
K-mer counting from fasta files with user defined k-mer size. Additionally, when provided with proper input data (see Usage), able to merge output data from the k-mer counting with resistance information to a machine learning friendly format. A script for training the data on the Random Forest algorithm is also included.

# Usage
Input requires assembled fasta files of the dataset that will be used for training the Random Forest algorithm. In theory raw reads should work, but I suspect the accuracy will suffer if raw reads are used. For the results shown here ABySS (2.3.7) was used with the following settings:

```
abyss-pe j=6 k=35 name=${accession} B=14G in="${file1} ${file2}" -C "${output_folder}/${accession}"
```

The k-mer counting program is usable with the command line by running 
```
GenomeML.py 
```
with appropiate options in the command line:

```
usage: GenomeML.py [-h] [-k KMER_SIZE] [-o OUTPUT_CSV] fasta_file

Extract k-mers from a fasta file and save to a csv file

positional arguments:
  fasta_file            Path to the fasta file

options:
  -h, --help            show this help message and exit
  -k KMER_SIZE, --kmer_size KMER_SIZE
                        Size of k-mers (default: 7)
  -o OUTPUT_CSV, --output_csv OUTPUT_CSV
                        Path to the output csv file (default: output.csv)
```

The command line only takes one input fasta file, but the program can be easily looped to take more. See 
```
GenomeML_run.sh
```
for a simple bash loop to analyze a dataset.

Be aware that increasing the k-mer size drastically increases the size of the output csv due to the vast increase of unique k-mers found for higher values of k. Using a dataset consisting of 586 assembled E. coli genomes, the merged output size was 44.6 MB with k=5, and increased to 1.1 GB with k=9. 

In order to use the merging function and Random Forest training script, your input should follow certain standards. First of all, the csv output files from GenomeML must have the following naming convention
```
 <sample_name>-contigs.csv
```
The sample names in turn have to correspond to sample names that are given in the file containing information on antibiotic resistance. See AMP_only_filtered.csv in example_data for an example on how this file must be formatted.

In 
```
merge_output.py
```
the variables folder and resistance_file should be changed to the path of the folder containing the csv output files from GenomeML and the path of your file containing resistance information. Additionally, edit output_csv to a path where to output should be written to.

# Ideas/to-do
At the moment the program only considers non-canonical k-mers. Can change this to support canonical k-mers to see if this improves performance.

Make the requirements of the data merging and Random Forest training not hard coded but dynamic.

# Data source
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6310291/#pcbi.1006258.s010

# References 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8722762/

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10809114/

