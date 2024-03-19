from collections import defaultdict

def extract_kmers(sequence, k):
    kmers = defaultdict(int)
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers[kmer] += 1
    return kmers

def main(fasta_file, k):
    with open(fasta_file, 'r') as f:
        sequence = ''
        for line in f:
            if line.startswith('>'):
                if sequence:
                    kmers = extract_kmers(sequence, k)
                    for kmer, count in kmers.items():
                        print(f'{kmer}\t{count}')
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            kmers = extract_kmers(sequence, k)
            for kmer, count in kmers.items():
                print(f'{kmer}\t{count}')

if __name__ == '__main__':
    fasta_file = '/home/sandervermeulen/Documents/GenomeML/test.fasta' # FASTA file
    k = 3  # kmer size
    main(fasta_file, k)

