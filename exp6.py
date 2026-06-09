from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

X = [
    [1],[2],[3],[8],[9],[10]
]

Y = [0,0,0,1,1,1]

model = GaussianNB()

model.fit(X,Y)

pred = model.predict(X)

print("Confusion Matrix")
print(confusion_matrix(Y,pred))

print("Accuracy")
print(accuracy_score(Y,pred))
