file = open('9_input.txt', 'r').readline()

#1
i = 0
new_file = ""
while i < len(file):
    marker_start = None
    marker_end = None
    if file[i] == '(':
        marker_start = i
        while file[i] != ')':
            i += 1
        i += 1
        marker_end = i
        marker = file[marker_start:marker_end]
        chars, times = [int(x) for x in marker.strip('()').split('x')]
        s = file[i:i + chars]
        ss = []
        for _ in range(times):
            ss.append(s)
        s_new = ''.join(ss)
        new_file += s_new
        i += len(s)
    else:
        i += 1

print(len(new_file))

