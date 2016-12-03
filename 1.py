ways = open('1_input.txt', 'r').readline().split(', ')

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
