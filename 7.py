import re

rows = open('7_input.txt', 'r').read().split('\n')

r = re.compile('(?P<hyper>\[\w*\])')


def find_abba(text):
    i = 0
    while i+4 <= len(text):
        a = text[i:i+4]
        if a[0] != a[1] and a == a[::-1]:
            return True
        i += 1
    return False


def find_aba(text):
    i = 0
    abas = []
    while i+3 <= len(text):
        a = text[i:i+3]
        if a[0] != a[1] and a == a[::-1]:
            abas.append(a)
        i += 1
    return abas

#1
count = 0
for row in rows:
    found = False
    hypers = r.findall(row)
    c = row
    for hyper in hypers:
        c = c.replace(hyper, '-')
        if find_abba(hyper):
            found = True

    if found:
        continue

    for s in c.split('-'):
        if find_abba(s):
            found = True

    if found:
        count += 1

print(count)

#2
count = 0
for row in rows:
    found = False
    hypers = r.findall(row)
    c = row
    for hyper in hypers:
        c = c.replace(hyper, '-')

    abas = []
    for s in c.split('-'):
        aba = find_aba(s)
        if aba:
            abas.extend(aba)

    for hyper in hypers:
        for aba in abas:
            bab = aba[1]+aba[0]+aba[1]
            if bab in hyper:
                found = True

    if found:
        count += 1

print(count)
