import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import linear_model

mydata = [[10,45],[16,98],[11,38],[16,93],[12,75],[13,95],[9,80],[2,10],[15,50]]

df1 = pd.DataFrame(mydata,columns=['hours','risk-score'])
print(df1)

X = df1.iloc[:,:-1]
y = df1.iloc[:,1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.5, random_state=1)

print(X_train)
print(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train.values,y_train.values)
print("Coef ::")
print(regressor.coef_)
print("intercept ::")
print(regressor.intercept_)

new = [[15]] 
print('predicated value of 15 hrs ')
print(regressor.predict(new))

y_pred = regressor.predict(X_test.values)
print('accuracy of LR model')
print(regressor.score(X_test.values,y_test.values))

plt.xlabel('hours')
plt.ylabel('risk-score')
plt.scatter(X_test,y_test,color='red',marker = '*') 
plt.plot(X_test,y_pred,color = 'grey') 
plt.plot(new,regressor.predict(new), color = 'red');