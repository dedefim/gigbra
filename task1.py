import re


pattern = r"[^a-zA-Z0-9_.]+@[a-zA-Z.]"
def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domen>\w+\.\w+)$')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'Проверьте правильность написания электронной почты: {email_address}')
    return result.groupdict()

print(email_parse('aaaaaaa@gmail.com'))
