import collections

rows = open('6_input.txt', 'r').read().split('\n')

bucks = []

for i in range(len(rows[0])):
    b = []
    for r in rows:
        b.append(r[i])
    bucks.append(b)

#1
print(''.join([y[0][0] for y in [collections.Counter(x).most_common(1) for x in bucks]]))

#2
print(''.join([y[0][0] for y in [collections.Counter(x).most_common()[-1] for x in bucks]]))
