from random import choice
def get_jokes(n,no_reput=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    res_one = []
    if no_reput:
        res_two = []
        for i in range(n):
            res_three = []
            if n > 5:
                no_reput = False
            if no_reput:
                new = choice(nouns)
                res_three.append(new)
                while new in res_two:
                    new = choice(nouns)
                    res_three.append(new)
                    new = choice(adverbs)
                while new in res_two:
                    new = choice(nouns)
                    res_three.append(new)
                    new = choice(adjectives)
                while new in res_two:
                    new = choice(adjectives)
                    res_three.append(new)
            else:
                res_three.append(choice(nouns))
                res_three.append(choice(adverbs))
                res_three.append(choice(adjectives))
            res_one.append(" ".join(res_three))
            if no_reput:
                res_one.extend(res_three)
        return res_one
print(get_jokes(n=3))
