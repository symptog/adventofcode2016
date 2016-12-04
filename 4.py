import re
import collections

rows = open('4_input.txt', 'r').read().split('\n')

abc = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, shift):
    return ''.join([abc[(abc.index(c)+shift) % 26] for c in text])


r = re.compile('^(?P<letters>[\w-]*)-(?P<sector>\d*)\[(?P<checksum>\w*)\]$')

sum = 0

for row in rows:
    m = r.match(row)
    letters = m.group('letters')
    sector = m.group('sector')
    checksum = m.group('checksum')
    top5 = collections.Counter(letters.replace('-', '')).most_common()
    top5_sorted = sorted(sorted(top5, key=lambda x: x[0], reverse=True), key=lambda x: x[1], reverse=False)[::-1]
    # print(top5_sorted)
    to_check = ''.join([x[0] for x in top5_sorted])[0:5]
    # print(to_check)
    if to_check == checksum:
        sum += int(sector)

    decoded_letters = ' '.join([caesar(x, int(sector)) for x in letters.split('-')])
    if 'north' in decoded_letters:
        print(sector, decoded_letters)

print(sum)
