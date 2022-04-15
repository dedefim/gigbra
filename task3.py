from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    list_1 = (items for items in zip_longest(tutors, klasses, fillvalue=None))
else:
    list_1 = (items for items in zip(tutors, klasses))
print(*list_1)
