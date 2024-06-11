#!/usr/bin/env python3

from collections import defaultdict
import csv

def reverse_complement(kmer):
    complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_bases[base] for base in reversed(kmer)) # Create reverse complement kmer

def extract_kmers(sequence, k, canonical_mode):
    kmers = defaultdict(int)
    for i in range(len(sequence) - k + 1): # Calculate number of kmers that can be extracted from seq
        if canonical_mode:
            kmer = sequence[i:i+k]
            rev_comp_kmer = reverse_complement(kmer)
            canonical_kmer = min(kmer, rev_comp_kmer)
            kmers[canonical_kmer] += 1
        else:
            kmer = sequence[i:i+k] # Extract all possible kmers from seq 
            kmers[kmer] += 1
    return kmers

def count_kmers(fasta_file, k, canonical_mode):
    total_kmers = defaultdict(int) # Empty dict to store kmer count
    with open(fasta_file, 'r') as f:
        sequence = ''
        for line in f:
            if line.startswith('>'): # To detect the fasta header
                if sequence: # Check if there is a sequence in the var, mainly for the first header
                    kmers = extract_kmers(sequence, k, canonical_mode)
                    for kmer, count in kmers.items():
                        total_kmers[kmer] += count # Update the dict with kmer count per contig
                    sequence = ''
            else:
                sequence += line.strip() # Add sequence to var, remove enters/whitespaces/etc.
        if sequence:
            kmers = extract_kmers(sequence, k, canonical_mode)
            for kmer, count in kmers.items():
                total_kmers[kmer] += count # Update the dict with kmer count per contig
    
    #sorted_kmers = sorted(total_kmers.items(), key=lambda x: x[1], reverse=False)
    
    #for kmer, count in sorted_kmers:
    	#print(f'K-mer: {kmer} Count: {count}')
    
    return total_kmers
    
def save_to_csv(total_kmers, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k-mer', 'count'])
        for kmer, count in total_kmers.items():
            writer.writerow([kmer, count])

