ways = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2".split(', ')
#        x, y
start = {
    'x': 0,
    'y': 0
}
#     0    1    2    3
d = ['N', 'O', 'S', 'W']
c = 0

punkte = []

for way in ways:
    direction = way[0]
    blocks = int(way[1::])
    if direction == "L":
        c = (c - 1) % 4
    else:
        c = (c + 1) % 4

    print("Gehe nach %s für %d Blöcke" % (d[c], blocks))
    for i in range(blocks):
        if c == 0:
            start['y'] += 1
        elif c == 1:
            start['x'] += 1
        elif c == 2:
            start['y'] -= 1
        elif c == 3:
            start['x'] -= 1

        punkt = (start['x'], start['y'])
        if punkt in punkte:
            print("Hier war ich schonmal")
            print("%d Blöcke entfernt." % (start['x'] + start['y']))
        punkte.append(punkt)

print("Easter Bunny HQ ist %d Blöcke entfernt." % (start['x'] + start['y']))
