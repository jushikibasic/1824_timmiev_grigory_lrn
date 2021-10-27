import re
RE_MAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9]+)+$')


def email_parse(email_address):
    if RE_MAIL.match(email_address):
        keys = ['username', 'domain']
        return dict(zip(keys, email_address.split('@')))
    else:
        raise ValueError(f'ValueError: wrong email: {email_address}')


print(email_parse('someone@geekbrains.ru'))
# print(email_parse('someone@geekbrainsru'))
