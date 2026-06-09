from sklearn.neural_network import MLPClassifier

X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

Y = [0,1,1,0]

model = MLPClassifier(
    hidden_layer_sizes=(4,),
    max_iter=5000,
    random_state=1
)

model.fit(X,Y)

print(model.predict([[1,0]]))
