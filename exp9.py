from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.array([1,2,3,4,5]).reshape(-1,1)
Y = np.array([1,4,9,16,25])

linear = LinearRegression()
linear.fit(X,Y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly,Y)

print("Linear:", linear.predict([[6]]))
print("Polynomial:", poly_model.predict(poly.transform([[6]])))
