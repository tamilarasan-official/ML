concepts = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']

specific = concepts[0].copy()

general = [['?' for i in range(len(specific))]
           for j in range(len(specific))]

for i, h in enumerate(concepts):

    if target[i] == 'Yes':
        for x in range(len(specific)):
            if h[x] != specific[x]:
                specific[x] = '?'
                general[x][x] = '?'

    else:
        for x in range(len(specific)):
            if h[x] != specific[x]:
                general[x][x] = specific[x]
            else:
                general[x][x] = '?'

print("Specific Hypothesis:")
print(specific)

print("General Hypothesis:")
for g in general:
    print(g)
