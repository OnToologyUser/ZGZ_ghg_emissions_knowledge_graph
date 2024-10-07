import sys 
import csv
import pandas as pd
import numpy as np
# Argument 1: File path
# Argument 2: Column name
# Argument 3: Fill value
with open(sys.argv[1], 'r') as f:
    header = next(csv.reader(f))
    
df = pd.read_csv(sys.argv[1], usecols=list(set(header)), dtype=object)
df[sys.argv[2]] = sys.argv[3] #np.nan
df.to_csv(sys.argv[1],index=False)
print ("Column: ", sys.argv[2], "values from file: ", sys.argv[1], " have been filled with: ", sys.argv[3]) 