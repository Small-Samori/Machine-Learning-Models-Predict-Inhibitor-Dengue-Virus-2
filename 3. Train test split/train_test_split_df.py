import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

actives = pd.read_csv('Dataset/active_molecular_descriptors.csv')
inactives = pd.read_csv('Dataset/imputed_inactives.csv')
inactives.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1, inplace=True)

print(actives.shape, inactives.shape)

ones = np.ones(actives.shape[0])
zeros = np.zeros(inactives.shape[0])

data = pd.concat([actives,inactives])
data.drop(['Name'], axis=1, inplace=True)

y = np.concatenate([ones,zeros])


X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=42)

X_train_df = pd.DataFrame(X_train, columns=data.columns)
X_test_df = pd.DataFrame(X_test, columns=data.columns)

y_train_df = pd.DataFrame(y_train)
y_test_df = pd.DataFrame(y_test)


X_train_df.to_csv('Dataset/X_train.csv', index=False)
X_test_df.to_csv('Dataset/X_test.csv', index=False)

y_train_df.to_csv('Dataset/y_train.csv', index=False)
y_test_df.to_csv('Dataset/y_test.csv', index=False)

print(X_train_df.shape, X_test_df.shape, y_train_df.shape, y_test_df.shape)
print(y_train_df.tail())
print(X_test_df.head())
