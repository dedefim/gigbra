def thesaurus(*args):
    name = dict()
    for names in args:
        letter = names[0]
        if letter not in name:
            name[letter] = []
        name[letter].append(names)
        return name
print(thesaurus("Иван", "Мария", "Пётр","Илья"))