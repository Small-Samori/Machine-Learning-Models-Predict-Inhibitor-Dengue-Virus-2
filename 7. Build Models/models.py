import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import matthews_corrcoef
from matplotlib.colors import ListedColormap
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import r2_score

scores = []
classificaiton_reports = []
mccs = []
r_squared_values = []
auc_values = []

names = [
         "Nearest Neighbors", 
         "Decision Tree", 
         "Random Forest", 
         "Neural Net", 
         "AdaBoost",
         "Naive Bayes", 
         "QDA"
         ]

classifiers = [
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    MLPClassifier(),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()
    ]


#X_train = pd.read_csv('Dataset 1/X_train_sm_reduced_standardized.csv')
#X_test = pd.read_csv('Dataset 1/X_test_reduced_standardized.csv')
#X_test.fillna(0, inplace=True)

X_train = pd.read_csv('Dataset/X_train_sm_reduced.csv')
X_test = pd.read_csv('Dataset/X_test_reduced.csv')
X_test.fillna(0, inplace=True)

y_train = pd.read_csv('Dataset/y_train_sm.csv')
y_test = pd.read_csv('Dataset/y_test.csv')


#X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.2,random_state =123)


# iterate over classifiers
for name, clf in zip(names, classifiers):
  clf.fit(X_train, y_train)

  y_preds = clf.predict(X_test)
  score = clf.score(X_test, y_test)
  scores.append(score)
  
  class_report = classification_report(y_test, y_preds)
  classificaiton_reports.append(class_report)
  
  mcc = matthews_corrcoef(y_test, y_preds)
  mccs.append(mcc)
  
  r_squared_value = r2_score(y_test, y_preds)
  r_squared_values.append(r_squared_value)
  
  fpr, tpr, thresholds = metrics.roc_curve(y_test, y_preds, pos_label=1)
  auc_value = metrics.auc(fpr,tpr)
  auc_values.append(auc_value)
  
  print(f"{name}: {score}")
  print(mcc)
  print(class_report)
  print(r_squared_value)
  print(auc_value)
  print('\n\n\n')
  
  with open(f"Evaluation/{name}_evaluatuin.txt",'w') as f:
    f.write(class_report)
    f.write('\n')
    
    f.write(f"MCC: {str(mcc)}")
    f.write('\n')
    
    f.write(f"R squared value: {str(r_squared_value)}")
    f.write('\n')
    
    f.write(f"AUC value: {str(auc_value)}")
    f.write('\n')
 

  
  
  

