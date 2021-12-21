import pandas as pd
from alive_progress import alive_bar
from imblearn.over_sampling import SMOTE

X_train = pd.read_csv('Dataset/X_train.csv')
X_train.fillna(0,inplace=True)

y_train = pd.read_csv('Dataset/y_train.csv')

print(y_train.value_counts())

smote = SMOTE(sampling_strategy='minority', random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

X_train_sm_df = pd.DataFrame(X_train_sm, columns=X_train.columns)
y_train_sm_df = pd.DataFrame(y_train_sm)

X_train_sm_df.to_csv('Dataset 2/X_train_sm.csv', index=False)
y_train_sm_df.to_csv('Dataset 2/y_train_sm.csv', index=False)

print(y_train_sm.value_counts())
print(X_train_sm_df.head())
print(y_train_sm_df)
