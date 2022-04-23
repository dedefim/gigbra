import os

ROOT = os.path.dirname(__file__)
data = os.path.join(ROOT, 'some_data')

result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files in os.walk(data):
    for file1 in files:
        size1 = os.stat((os.path.join(root, file1))
        if  size1 == 0:
            result[0] += 1
            continue
    for len1, key in enumerate(keys):
        if len1  == len(keys) - 1:
            print(f"{file1}")
            break
        if key < size1 <= keys[len1 + 1]:
            result[keys[len1 + 1]] += 1
print(result)
