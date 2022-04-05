list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for i in list_1:
    if i.isdigit() and len(i) == 1:
         i = f'0{i}'
         list_2.append('"')
         list_2.append(i)
         list_2.append('"')
    elif len(i) == 2 and not i[0].isdigit():
        i = f'{i[0]}0{i[1]}'
        list_2.append('"')
        list_2.append(i)
        list_2.append('"')
    elif len(i) == 2:
     list_2.append('"')
     list_2.append(i)
     list_2.append('"')
    else:
        list_2.append(i)
print(' '.join(list_2))
