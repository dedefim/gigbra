a = int(input("Введите делимое число: "))
b = int(input("Введите делитель: "))
try:
    quotient = a / b
    print(quotient)
except ZeroDivisionError:
    print("Я не умею делить на 0")
