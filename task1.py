result = []
with open('nginx_logs.txt', 'r', encoding= 'utf-8') as fail:
    for line in fail:
        line_1 = line.split()
        result.append((line_1[0], line_1[5].split('"'), line_1[6]))
print(result)
