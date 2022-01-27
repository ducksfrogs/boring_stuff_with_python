import re


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'mmmm 000-1111-2222 dddd 222-222-3333 dddd ddddd 000-222-44444'

for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Found phone_number: " + chunk)
print("Fin")

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search(message)

for i in range(2):
    mo.group()
