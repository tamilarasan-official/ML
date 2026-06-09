concepts = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']

hypothesis = concepts[0].copy()

for i in range(len(concepts)):
    if target[i] == 'Yes':
        for j in range(len(hypothesis)):
            if hypothesis[j] != concepts[i][j]:
                hypothesis[j] = '?'

print("Final Hypothesis:")
print(hypothesis)
