#!/bin/bash

# Path to the downloaded files
download_dir="/media/sf_Project_GenomeML/Assembled"
output_folder="/home/sandervermeulen/Documents/Ecoli_assembled"

# Loop over the directories in the download directory
for dir in "$download_dir"/*; do
    # Check if it's a directory
    if [ -d "$dir" ]; then
        # Extract the accession number from the directory name
        accession="$(basename "$dir")"
        
        # Check if the folder is already present and skip if true
        if [ -d "$output_folder/$accession" ]; then
        
        echo "Folder ${output_folder}/${accession} already exists."
        
        # Check if the accession number has a subdirectory              
        elif [ -d "$dir/$accession" ]; then
            # Accession number has a subdirectory structure
            
            # Get the two file paths in the subdirectory
            file1="${dir}/${accession}/${accession}_1.fastq.gz"
            file2="${dir}/${accession}/${accession}_2.fastq.gz"
            
            mkdir $output_folder/$accession
            
            # Run Abyss using the input files in the subdirectory
            abyss-pe j=6 k=35 name=${accession} B=14G in="${file1} ${file2}" -C "${output_folder}/${accession}"
            
        else
            # Accession number does not have a subdirectory structure
            
            # Get the two file paths in the directory
            file1="${dir}/${accession}_1.fastq.gz"
            file2="${dir}/${accession}_2.fastq.gz"
            
            mkdir $output_folder/$accession
            
            # Run Abyss using the input files in the subdirectory
            abyss-pe j=6 k=35 name=${accession} B=14G in="${file1} ${file2}" -C "${output_folder}/${accession}"
            
        fi
    fi
done

