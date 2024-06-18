#!/usr/bin/env python3

from collections import defaultdict
import csv

def reverse_complement(kmer):
    complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    try:
        return ''.join(complement_bases[base] for base in reversed(kmer)) # Create reverse complement kmer
    except KeyError:
        return None # Ignore k-mers with hard and soft masked bases

def extract_kmers(sequence, k, canonical_mode):
    kmers = defaultdict(int)
    ignored_kmers = 0
    for i in range(len(sequence) - k + 1): # Calculate number of kmers that can be extracted from seq
        if canonical_mode:
            kmer = sequence[i:i+k]
            rev_comp_kmer = reverse_complement(kmer)
            if rev_comp_kmer is None:
                ignored_kmers += 1 # Count number of kmers that are ignored due to masking
            else:
                canonical_kmer = min(kmer, rev_comp_kmer)
                kmers[canonical_kmer] += 1
        else:
            kmer = sequence[i:i+k] # Extract all possible kmers from seq 
            kmers[kmer] += 1
    return kmers, ignored_kmers

def count_kmers(fasta_file, k, canonical_mode):
    total_kmers = defaultdict(int) # Empty dict to store kmer count
    total_ignored_kmers = 0
    with open(fasta_file, 'r') as f:
        sequence = ''
        for line in f:
            if line.startswith('>'): # To detect the fasta header
                if sequence: # Check if there is a sequence in the var, mainly for the first header
                    kmers, ignored_kmers = extract_kmers(sequence, k, canonical_mode)
                    total_ignored_kmers += ignored_kmers
                    for kmer, count in kmers.items():
                        total_kmers[kmer] += count # Update the dict with kmer count per contig
                    sequence = ''
            else:
                sequence += line.strip() # Add sequence to var, remove enters/whitespaces/etc.
        if sequence:
            kmers, ignored_kmers = extract_kmers(sequence, k, canonical_mode)
            total_ignored_kmers += ignored_kmers
            for kmer, count in kmers.items():
                total_kmers[kmer] += count # Update the dict with kmer count per contig
    
    #sorted_kmers = sorted(total_kmers.items(), key=lambda x: x[1], reverse=False)
    
    #for kmer, count in sorted_kmers:
    	#print(f'K-mer: {kmer} Count: {count}')
    
    print(f"Ignored k-mers due to masking: {total_ignored_kmers}")
    return total_kmers
    
def save_to_csv(total_kmers, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k-mer', 'count'])
        for kmer, count in total_kmers.items():
            writer.writerow([kmer, count])

