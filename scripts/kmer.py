from collections import defaultdict

def extract_kmers(sequence, k):
    kmers = defaultdict(int)
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers[kmer] += 1
    return kmers

def main(fasta_file, k):
    total_kmers = defaultdict(int) # Empty dict to store kmer count
    with open(fasta_file, 'r') as f:
        sequence = ''
        for line in f:
            if line.startswith('>'): # To filter fasta header 
                if sequence: # Check if there is a sequence in the var
                    kmers = extract_kmers(sequence, k)
                    for kmer, count in kmers.items():
                        total_kmers[kmer] += count # Update the dict with kmer count per contig
                    sequence = ''
            else:
                sequence += line.strip() # Add sequence to var, remove enters/whitespaces/etc.
        if sequence:
            kmers = extract_kmers(sequence, k)
            for kmer, count in kmers.items():
                total_kmers[kmer] += count # Update the dict with kmer count per contig
    
    sorted_kmers = sorted(total_kmers.items(), key=lambda x: x[1], reverse=False)
    
    for kmer, count in sorted_kmers:
    	print(f'K-mer: {kmer} Count: {count}')
    	
    return total_kmers

if __name__ == '__main__':
    fasta_file = '/home/sandervermeulen/Documents/GenomeML/Ecoli_assembled/ERR1218534/ERR1218534-contigs.fa' # Fasta file path
    k = 13  # kmer size
    total_counts = main(fasta_file, k)
    print("Total k-mers:", sum(total_counts.values()))

