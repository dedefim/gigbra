import sys
import json


result = dict()
with open('users.csv', 'r', encoding='utf-8') as f_1, \
      open('hobby.csv', 'r', encoding='utf-8') as f_2:
    for line_1 in f_1:
        line_2 = f_2.readline().strip()
        if not line_2:
            line_2 = None
        if line_1 not in result:
            result[line_1.strip()] = line_2
    content = f_2.read()
    if content:
        sys.exit(1)
with open('result.json', 'w', encoding='utf-8') as result_fail:
    dict_1 = json.dumps(result, ensure_ascii=False)
print(result)
