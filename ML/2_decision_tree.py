import pandas as pd
import numpy as np

df = pd.read_csv('cosmetics.csv')

print(df)

x = df.iloc[:,1:5]
y = df.iloc[:,5]

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
x=x.apply(le.fit_transform)
print(x)

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier = classifier.fit(x.values,y.values)

classifier.predict([[1,1,0,0]])

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,8))
tree.plot_tree(classifier)

