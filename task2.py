MAX_NUM = int(input('Введите число: '))
nums_gen = (num for num in range(1, MAX_NUM + 1, 2))
print(*nums_gen)
