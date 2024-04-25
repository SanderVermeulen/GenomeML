#!/usr/bin/env python3

import os
import pandas as pd

def merge_csv_files(folder):
    merged_df = pd.DataFrame()  # Create empty df to store merged data

    # Loop through all csv files in the folder
    for file_name in os.listdir(folder):
        if file_name.endswith(".csv"): # Only consider csv files
            file_path = os.path.join(folder, file_name)
            
            df = pd.read_csv(file_path) 
                      
            sample_name = file_name.split("-")[0] # Get sample name from filename
            
            df.set_index('k-mer', inplace=True) # Set index of df to k-mer column
            
            df.rename(columns={'count': sample_name}, inplace=True) # Rename count column to sample name
            
            merged_df = pd.concat([merged_df, df], axis=1, sort=False)

    merged_df.fillna(0, inplace=True) # Fill NaN with 0
    
    merged_df = merged_df.transpose()
    
    merged_df.index.name = None
    
    merged_df.reset_index(inplace=True) # Make k-mer column a normal column
    
    return merged_df

# Folder containing csv files from GenomeML
folder = "/home/sandervermeulen/Documents/GenomeML/Ecoli_kmers/kmer_7/"

merged_df = merge_csv_files(folder)

# Read the resistance information csv file into a df
resistance_file = "/media/sf_Project_GenomeML/Accessions_scripts/AMP_only_filtered.csv"
resistance_df = pd.read_csv(resistance_file)

# Merge the k-mer df with the resistance information df based on 'Lane.accession'
merged_df = pd.merge(merged_df, resistance_df, left_on='index', right_on='Lane.accession', how='left')

# Map the resistance labels ('R' and 'S') to numerical values (0 and 1)
merged_df['Resistance'] = merged_df['AMP'].map({'R': 0, 'S': 1})

# Drop unnecessary columns
merged_df.drop(columns=['ENA.Accession.Number', 'Isolate', 'Lane.accession', 'AMP'], inplace=True)

# Save the merged df to a new csv file
output_csv = "/home/sandervermeulen/Documents/GenomeML/Ecoli_kmers/kmer_7/output_kmer7_res.csv"
merged_df.to_csv(output_csv, index=False)
