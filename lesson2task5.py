basket = [57.8, 46.51, 97, 900,  86, 3, 76, 8000, 678, 10, 11, 12.89, 6.6]
basket_1 = []
for i in basket:
    money = int(round(i * 100))
    rub = money // 100
    cop = money % 100
    basket_1.append(f'{rub} руб {cop:02d} коп')
print(' '.join(basket_1))
test = id(basket)
basket.sort()
print(basket)
print(id(basket) == test)
test_2 = sorted(basket, reverse=True)
print(test_2)
print(test_2[:5])
