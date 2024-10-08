import sys 
import csv
import pandas as pd
import numpy as np
# Argument 1: Column name
# Argument 2: File path
with open(sys.argv[2], 'r') as f:
    header = next(csv.reader(f))
    
df = pd.read_csv(sys.argv[2], usecols=list(set(header) - {sys.argv[1]}), dtype=object)
df[sys.argv[1]] = np.nan
df.to_csv(sys.argv[2])
print ("Column: ", sys.argv[1], " has been filled with blank values from file: ", sys.argv[2]) 