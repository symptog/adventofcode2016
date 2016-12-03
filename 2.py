rows = open('2_input.txt', 'r').read().split('\n')

keypad1 = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
]

keypad2 = [
    [None, None,   1, None, None],
    [None,    2,   3,    4, None],
    [   5,    6,   7,    8,    9],
    [None,  "A", "B",  "C", None],
    [None, None, "D", None, None]
]

result1 = []
result2 = []

start = [1, 1]

# 1
for r in rows:
    for c in r:
        if c == 'D':
            if start[0] < 2:
                start[0] += 1
        if c == 'U':
            if start[0] > 0:
                start[0] -= 1
        if c == 'R':
            if start[1] < 2:
                start[1] += 1
        if c == 'L':
            if start[1] > 0:
                start[1] -= 1
    result1.append(keypad1[start[0]][start[1]])

print(''.join([str(x) for x in result1]))

start = [2, 0]
# 2
for r in rows:
    for c in r:
        if c == 'D':
            if start[0] < 4 and keypad2[start[0]+1][start[1]]:
                start[0] += 1
        if c == 'U':
            if start[0] > 0 and keypad2[start[0] - 1][start[1]]:
                start[0] -= 1
        if c == 'R':
            if start[1] < 4 and keypad2[start[0]][start[1] + 1]:
                start[1] += 1
        if c == 'L':
            if start[1] > 0 and keypad2[start[0]][start[1] - 1]:
                start[1] -= 1
    result2.append(keypad2[start[0]][start[1]])

print(''.join([str(x) for x in result2]))
