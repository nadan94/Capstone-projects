import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Data sets for the average hourly rate for a female employee based on age

#Training set
x_train = [[20], [26], [31], [36], [41], [46], [51], [56]]
y_train = [[22.92], [29.90], [31.43], [34.90], [36.05], [36.57], [37.19], [36.57]]

#Testing set
x_test = [[61], [66], [70]] 
y_test = [[34.91], [33.09], [30.80]]


xx = np.linspace(0, 70, 100)

#Set the degree of the polynomial regression model
polyFeatures = PolynomialFeatures(degree=2)

#Transforms into matrix of given degree
xTrainQuadratic = polyFeatures.fit_transform(x_train)
xTestQuadratic = polyFeatures.transform(x_test)

#Train and test model
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(xTrainQuadratic, y_train)
xx_quadratic = polyFeatures.transform(xx.reshape(xx.shape[0], 1))

#plot the graph                                      
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Average hourly rate')
plt.scatter(x_train, y_train)
plt.show()
