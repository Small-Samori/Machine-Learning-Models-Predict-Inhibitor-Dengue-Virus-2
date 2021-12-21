from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

X_train_sm_reduced = pd.read_csv('Dataset 1/X_train_sm_reduced.csv')
X_test_reduced = pd.read_csv('Dataset 1/X_test_reduced.csv')
X_test_reduced.fillna(0,inplace=True)

X_train_sm_reduced_normalized = normalize(X_train_sm_reduced)
X_train_sm_reduced_normalized = pd.DataFrame(X_train_sm_reduced_normalized, 
						columns=X_train_sm_reduced.columns)

X_test_reduced_normalized = normalize(X_test_reduced)
X_test_reduced_normalized = pd.DataFrame(X_test_reduced_normalized, 
						columns=X_test_reduced.columns)	

X_train_sm_reduced_normalized.to_csv('Dataset 1/X_train_sm_reduced_normalized.csv', index=None)
X_test_reduced_normalized.to_csv('Dataset 1/X_test_reduced_normalized.csv', index=None)	

print(X_train_sm_reduced_normalized.shape, X_test_reduced_normalized.shape)
