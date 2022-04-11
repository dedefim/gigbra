def num_translate(word):
   number = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'}
   if word.istitle() and number.get(word.lower()):
       return number.get(word.lower()).title()
   else:
    return number.get(word)
print(num_translate(input('Введите слово: ')))
