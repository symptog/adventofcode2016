rows = open('3_input.txt', 'r').read().split('\n')

tris = [[int(y) for y in z] for z in [x.strip().split() for x in rows]]
print(tris)
#1
not_failed = 0

for tri in tris:
    a, b, c = tri

    if (a + b > c) and (a + c > b) and (b + c > a):
        not_failed += 1

print(not_failed)

#2
not_failed = 0
tris = tris[::-1]

while tris:
    tris2 = []
    for _ in range(3):
        tris2.append(tris.pop())
    for i in range(3):
        a = tris2[0][i]
        b = tris2[1][i]
        c = tris2[2][i]
        if (a + b > c) and (a + c > b) and (b + c > a):
            not_failed += 1

print(not_failed)
