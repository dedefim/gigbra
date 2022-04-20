result = []
dict_1 = dict()
with open('nginx_logs.txt', 'r', encoding= 'utf-8') as fail:
    for line in fail:
        line_1 = line.split()
        ip = line_1[0]
        if ip not in dict_1:
            dict_1[ip] = 1
        else:
            dict_1[ip] += 1
print(result)
m = 0
k = ''
for key, value in dict_1.items():
    if value > m:
        k = key
print(k, m)
