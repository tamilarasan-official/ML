from sklearn.tree import DecisionTreeClassifier

X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

Y = [0,1,1,0]

model = DecisionTreeClassifier(criterion='entropy', random_state=0)

model.fit(X,Y)

prediction = model.predict([[1,0]])

print("Prediction:", prediction[0])
