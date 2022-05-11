import numpy as np
import pandas as pd

dataset = pd.read_csv("Kdata.csv")

print (dataset)

X = dataset.iloc[:,:-1].values
X

y = dataset.iloc[:,2].values
y

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)

X_test=np.array([6,6])
y_pred=classifier.predict([X_test])

print ('general KNN:',y_pred)

classifier=KNeighborsClassifier(n_neighbors=3,weights='distance')

classifier.fit(X,y)

"""#predict class for the points (6,6)"""

X_test=np.array([6,6])
y_pred=classifier.predict([X_test])

print ('Distance weighted KNN:',y_pred)