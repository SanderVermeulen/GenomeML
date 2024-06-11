#!/usr/bin/env python3

import argparse
import os
from kmer import count_kmers, save_to_csv

def parse_args():
    parser = argparse.ArgumentParser(description="Extract k-mers from a fasta file and save to a csv file")
    parser.add_argument("fasta_file", help="Path to the fasta file")
    parser.add_argument("-k", "--kmer_size", type=int, default=7, help="Size of k-mers (default: 7)")
    parser.add_argument("-o", "--output_csv", default="output.csv", help="Path to the output csv file (default: output.csv)")
    parser.add_argument("-c", "--canonical", action='store_true', help="Enable canonical k-mer counting mode")
    return parser.parse_args()

def main():
    args = parse_args()
    fasta_file = args.fasta_file
    kmer_size = args.kmer_size
    output_csv = args.output_csv
    canonical_mode = args.canonical
    
    if not os.path.exists(fasta_file): # Checking if the fasta file exists
        print(f"Error: fasta file '{fasta_file}' not found.")
        sys.exit(1)
    
    if canonical_mode:
        print("Canonical mode enabled")
    else:
        print("Canonical mode disabled")

    total_counts = count_kmers(fasta_file, kmer_size, canonical_mode)
    save_to_csv(total_counts, output_csv)
    print(f"K-mers saved to {output_csv}")

if __name__ == "__main__":
    main()
