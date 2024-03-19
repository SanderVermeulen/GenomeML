#!/bin/bash

# Path to the accession list file
accession_list="accession_list.txt"

# Output directory
output_dir="/mnt/h/Ubuntu/Project_GenomeML/Data/"

# Read the accession list file line by line
while IFS= read -r accession; do
    # Check the accession number prefix
    if [[ $accession == ERR434* ]] || [[ $accession == ERR435* ]] || [[ $accession == ERR439* ]]; then
        # Construct the FTP URL for ERR434, ERR435, and ERR439
        ftp_url="ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${accession:0:6}/${accession}/"
    else
        # Extract the last digit of the accession number
        last_digit="${accession: -1}"
        
        # Construct the middle folder with leading zeros
        middle_folder=$(printf "%03d" "${last_digit}")
        
        # Construct the FTP URL for ERR121
        ftp_url="ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR121/${middle_folder}/${accession}/"
    fi
    
    # Create the output directory for the accession
    accession_dir="${output_dir}/${accession}/"
    mkdir -p "${accession_dir}"
    
    # Download the entire folder using wget
    wget --continue --no-host-directories --cut-dirs=4 --recursive --level=1 --directory-prefix="${accession_dir}" "${ftp_url}"
done < "$accession_list"
