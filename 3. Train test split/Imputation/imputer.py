import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

inactives = pd.read_csv('inactives.csv')
print(inactives.shape)

#na_summary = inactives.isna().sum()


#na_cols = []

#for i in range(len(na_summary)):
#	if na_summary[i] != 0:
#		na_cols.append(na_summary.index[i])

#with open('na_cols.txt', 'w') as f:
#	for col in na_cols:
#		f.write(col)
#		f.write("\n")


imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_inactives = imp_mean.fit_transform(inactives)
print(imp_inactives.shape)

imp_inactives_df = pd.DataFrame(imp_inactives, columns=inactives.columns)
print(imp_inactives_df.shape)
imp_inactives_df.to_csv('imp_inactives.csv')

print(imp_inactives.shape, imp_inactives_df.shape, inactives.shape)

