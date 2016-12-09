import re

rows = open('8_input.txt', 'r').read().split('\n')

r = re.compile('rect (?P<rect>\d*x\d*)|rotate[\w\s]*(?P<rot>[xy]=\d*)\s*by\s*(?P<by>\d*)')

display = []

for i in range(6):
    a = []
    for j in range(50):
        a.append(' ')
    display.append(a)


def fill(x, y):
    for i in range(y):
        for j in range(x):
            display[i][j] = '#'


def rot_col(col):
    l = display[-1][col]
    for i in range(len(display)-1)[::-1]:
        display[i + 1][col] = display[i][col]
    display[0][col] = l


def rot_row(row):
    l = display[row][-1]
    for i in range(len(display[row])-1)[::-1]:
        display[row][i + 1] = display[row][i]
    display[row][0] = l

for row in rows:
    rect, rot, by = r.match(row).groups()
    if rect:
        x, y = [int(a) for a in rect.split('x')]
        fill(x, y)
    if rot and by:
        d, c = rot.split('=')
        if d == 'x':
            for _ in range(int(by)):
                rot_col(int(c))
        if d == 'y':
            for _ in range(int(by)):
                rot_row(int(c))

count = 0
for d in display:
    for c in d:
        if c == '#':
            count += 1
    print(''.join(d))

print(count)
