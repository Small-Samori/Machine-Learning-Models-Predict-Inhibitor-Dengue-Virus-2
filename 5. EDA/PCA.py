import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from sklearn.decomposition import PCA

def pca_DataFrame(X, y):
	pca = PCA()
	X_pca = pca.fit_transform(X,y)
	X_pca_df = pd.DataFrame(X_pca, columns=['pc'+ i for i in list(map(str,range(1,X.shape[1]+1)))])

	return X_pca_df

def pca_plot(X, y, title):
	print(X.shape)
	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 15)
	ax.set_ylabel('Principal Component 2', fontsize = 15)
	ax.set_title(title, fontsize = 20)
	targets = [1, 0]
	colors = ['r', 'b']
	#bar = IncrementalBar('Countdown', max = len(colors))
	for target, color in zip(targets,colors):
		#bar.next()
		indicesToKeep = y == target
		ax.scatter(X.loc[indicesToKeep, 'pc1'], 
		X.loc[indicesToKeep, 'pc2'], 
		c = color, s = 10)
	#bar.finish()
	ax.legend(['Active','Inactive'])
	ax.grid()
	#plt.xlim([0.0,0.3])
	plt.savefig(f"{title}.jpg")

train_X = pd.read_csv('Dataset/X_train_sm.csv')
train_y = pd.read_csv('Dataset/y_train_sm.csv')

test_X = pd.read_csv('Dataset/X_test.csv')
test_y = pd.read_csv('Dataset/y_test.csv')

data = train_X.append(test_X)
data.fillna(0, inplace=True)
data_y = train_y.append(test_y)

print(train_X.shape, test_X.shape, data.shape)

data_pca = pca_DataFrame(data,data_y)

pca_plot(data_pca, data_y.values, 'Two component PCA of Actives and Inactives')
