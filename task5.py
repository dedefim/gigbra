src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
vocabulary = {}
for j in src:
    if j in vocabulary:
        vocabulary[j] += 1
    else:
        vocabulary[j] = 1
result = [i for i in src if vocabulary[i] == 1]
print(result)
