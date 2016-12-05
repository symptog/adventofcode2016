import re
from hashlib import md5

puzzle = "reyedfim"

#1
r = re.compile('^00000([a-h0-9])')
i = 0
result = ""

while len(result) < 8:
    to_hash = "%s%d" % (puzzle, i)
    h = md5(str(to_hash).encode('utf-8')).hexdigest()
    m = r.match(h)
    if m:
        result += m.groups()[0]

    i += 1

print(result)

#2
r = re.compile('^00000([0-7])([a-h0-9])')
i = 0
result = [None, None, None, None, None, None, None, None]

while None in result:
    to_hash = "%s%d" % (puzzle, i)
    h = md5(str(to_hash).encode('utf-8')).hexdigest()
    m = r.match(h)
    if m:
        pos = int(m.groups()[0])
        c = m.groups()[1]
        if result[pos] is None:
            result[pos] = c
    i += 1

print(''.join(result))
