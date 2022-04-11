def currency_rates(word):
    from requests import get
    rest = get('http://www.cbr.ru/scripts/XML_daily.asp')
    code = rest.text
    codes = []
    praice = []
    for el in code.split('<CharCode>')[1:]:
        a = el.split('</CharCode>')[0]
        codes.append(a)
    for i in code.split('<Value>')[1:]:
        b = i.split('</Value>')[0]
        praice.append(b)
    parity = dict(zip(codes, praice))
    return parity.get(word.upper())
if __name__ == "__main__":
    print(currency_rates(input('Введите код валюты: ')))