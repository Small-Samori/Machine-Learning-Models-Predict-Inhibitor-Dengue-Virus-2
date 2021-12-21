import pandas as pd

actives = pd.read_csv('active_smile_activity_data.csv')
inactives = pd.read_csv('inactive_smile_activity_data.csv')

column_selection = ['SMILES','PUBCHEM_SID']

active_smi_df = actives[column_selection]
inactive_smi_df_1 = inactives[column_selection].loc[:199999]
inactive_smi_df_2 = inactives[column_selection].loc[200000:]

inactive_smi_df_1.reset_index(drop=True, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([27117], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([47576], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([62776], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([62777], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([113280], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([113280], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop(range(113644,113661), axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

inactive_smi_df_2.drop([113644], axis=0, inplace=True)
inactive_smi_df_2.reset_index(drop=True, inplace=True)

active_smi_df.to_csv('active smi/actives.smi', sep='\t', index=False, header=False)
inactive_smi_df_1.to_csv('inactive_2 smiinactives_1.smi', sep='\t', index=False, header=False)
inactive_smi_df_2.to_csv('inactive_2 smi/inactives_2.smi', sep='\t', index=False, header=False)

#print(inactive_smi_df_2.shape)
print(active_smi_df.shape,inactive_smi_df_1.shape, inactive_smi_df_2.shape)
#print(inactive_smi_df_2.iloc[474])
