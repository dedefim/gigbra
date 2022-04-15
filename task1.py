

def nums_gen(MAX_NUM):
    for num in range(1, MAX_NUM + 1, 2):
        yield num


print(*nums_gen(int(input('Введите число: '))))
