import pandas as pd

datatable = pd.read_csv("AID_651640_datatable_all.csv")
smiles_data = pd.read_csv("smiles_dataset_csv.csv")

selected_columns = ['PUBCHEM_SID', 'PUBCHEM_ACTIVITY_OUTCOME',
                    'PUBCHEM_ACTIVITY_SCORE']

metadata = datatable[selected_columns]
metadata.drop(range(4), inplace=True)
metadata.drop(range(261940, 261945), inplace=True)
metadata.reset_index(drop=True, inplace=True)


merged_data = metadata.join(smiles_data.set_index('PUBCHEM_SID'), on='PUBCHEM_SID')
merged_data.to_csv(r'smile_activity_data.csv', index=None)


print(smiles_data.shape, metadata.shape, merged_data.shape)
