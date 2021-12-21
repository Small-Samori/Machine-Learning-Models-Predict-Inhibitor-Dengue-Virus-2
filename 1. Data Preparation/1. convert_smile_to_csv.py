import pandas as pd

smile_format = pd.read_csv(r'smiles_dataset_txt.txt', sep='\t', header=None)
smile_format.columns = ['PUBCHEM_SID', 'SMILES']
smile_format.to_csv(r'smiles_dataset_csv.csv', index=None)
