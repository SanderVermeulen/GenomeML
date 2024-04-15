from collections import defaultdict
import csv

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
    	

if __name__ == '__main__':
    fasta_file = '/home/sandervermeulen/Documents/GenomeML/Ecoli_assembled/ERR1218534/ERR1218534-contigs.fa' # Fasta file path
    k = 9  # kmer size
    
    total_counts = main(fasta_file, k)
    #print("Total k-mers:", sum(total_counts.values()))
    
    csv_file = '/home/sandervermeulen/Documents/GenomeML/Ecoli_kmers/test.csv'
    save_to_csv(total_counts, csv_file)
    print(f"K-mers saved to {csv_file}")

