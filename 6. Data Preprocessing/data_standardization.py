from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

X_train_sm_reduced = pd.read_csv('Dataset/X_train_sm_reduced.csv')
X_test_reduced = pd.read_csv('Dataset/X_test_reduced.csv')

scaler = StandardScaler()
X_train_sm_reduced_standardized = scaler.fit_transform(X_train_sm_reduced)
X_train_sm_reduced_standardized = pd.DataFrame(X_train_sm_reduced_standardized, 
						columns=X_train_sm_reduced.columns)

X_test_reduced_standardized = scaler.transform(X_test_reduced)
X_test_reduced_standardized = pd.DataFrame(X_test_reduced_standardized, 
						columns=X_test_reduced.columns)	

X_train_sm_reduced_standardized.to_csv('Dataset/X_train_sm_reduced_standardized.csv', index=None)
X_test_reduced_standardized.to_csv('Dataset/X_test_reduced_standardized.csv', index=None)	

print(X_train_sm_reduced_standardized.shape, X_test_reduced_standardized.shape)
