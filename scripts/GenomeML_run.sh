#!/bin/bash

folder="$HOME/Documents/GenomeML"

for f in $(find "$folder" -path '*/Ecoli_assembled/ERR*/*-contigs.fa'); do
    filename=$(basename "$f")
    output_csv="$folder/Ecoli_kmers/kmer_7/${filename%.fa}.csv"
    ./GenomeML.py -k 7 -o "$output_csv" "$f"
done

