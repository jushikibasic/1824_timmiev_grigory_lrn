import re

RE_MAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9]+)+$')


def email_parse(email_address):
    if RE_MAIL.match(email_address):
        keys = ['username', 'domain']
        tmp = email_address.split('@')
        result = dict(zip(keys, tmp))
        return result
    else:
        msg = f'ValueError: wrong email:{email_address}'
        raise ValueError(msg)


print(email_parse('someone@geekbrainsru'))
