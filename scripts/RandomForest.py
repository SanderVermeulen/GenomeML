#!/usr/bin/env python3


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

def train_random_forest(csv_file):
    df = pd.read_csv(csv_file)
    df = df.drop(columns=['index']) # Drop index column since this contains the name of the samples, not training features
    
    X = df.drop(columns=['Resistance']) # Features, k-mers counts
    y= df['Resistance'] # Labels, resistant or susceptible
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    
csv_file = "/home/sandervermeulen/Documents/GenomeML/Ecoli_kmers/kmer_7/output_kmer7_res.csv"

train_random_forest(csv_file)
