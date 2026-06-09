from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5],[6]]
Y = [0,0,0,1,1,1]

model = LogisticRegression()

model.fit(X,Y)

print(model.predict([[5]]))
