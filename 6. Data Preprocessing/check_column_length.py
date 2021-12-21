import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed
from numpy.random import randn
from scipy.stats import mannwhitneyu
from progress.bar import Bar


def mannwhitney(data, descriptor, verbose=False):
  # https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/

	# seed the random number generator
	seed(1)

	# actives and inactives
	selection = [descriptor, '0']
	df = data[selection]
	
	active = df[df['0'] == 1][descriptor]
	inactive = df[df['0'] == 0][descriptor]

	# compare samples
	if list(active) == list(inactive):
		results = pd.DataFrame({'Descriptor':descriptor,
				  'Statistics':'-',
				  'p':'-',
				  'alpha':'-',
				  'Interpretation':'Same distribution (fail to reject H0)'}, index=[0])
		return results
		
	stat, p = mannwhitneyu(active, inactive)

	# interpret
	alpha = 0.05
	if p > alpha:
		interpretation = 'Same distribution (fail to reject H0)'
		results = pd.DataFrame({'Descriptor':descriptor,
				  'Statistics':stat,
				  'p':p,
				  'alpha':alpha,
				  'Interpretation':interpretation}, index=[0])
	else:
		interpretation = 'Different distribution (reject H0)'
		results = pd.DataFrame({'Descriptor':descriptor,
				  'Statistics':stat,
				  'p':p,
				  'alpha':alpha,
				  'Interpretation':interpretation}, index=[0])

	return results
	




def reduce_dataset(data):
	cols_to_keep = []

	results_dataframes_status = False

	with Bar('Loading', fill='#', suffix='%(percent).1f%% - %(eta)ds') as bar:
		for descriptor in data.columns:

			descriptor_result = mannwhitney(data,descriptor)
			
			a = descriptor_result['Interpretation'] == 'Different distribution (reject H0)'
			if a.item():
				cols_to_keep.append(descriptor)
				
			if results_dataframes_status:
				test_results = pd.concat([test_results, descriptor_result])
			else:
				test_results = descriptor_result
				results_dataframes_status = True
			bar.next()
	
	return cols_to_keep, test_results



X_train_sm = pd.read_csv('Dataset 1/X_train_sm.csv')
y_train_sm = pd.read_csv('Dataset 1/y_train_sm.csv')

X_test = pd.read_csv('Dataset 1/X_test.csv')
y_test = pd.read_csv('Dataset 1/y_test.csv')


train_data = pd.concat([X_train_sm, y_train_sm], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

train_col, train_mannwhitneyu_results = reduce_dataset(train_data)
#test_col, test_test_results = reduce_dataset(test_data)

print(len(train_col))

#X_train_sm_reduced = X_train_sm[train_col]
#X_test_reduced = X_test[train_col]

#print(len(train_col))
#print(X_train_sm.shape, X_train_sm_reduced.shape)
#print(X_test.shape, X_test_reduced.shape)

#X_train_sm_reduced.to_csv('Dataset 1/X_train_sm_reduced.csv', index=None)
#X_test_reduced.to_csv('Dataset 1/X_test_reduced.csv', index=None)
#train_mannwhitneyu_results.to_csv('train_mannwhitneyu_results.csv', index=None)

