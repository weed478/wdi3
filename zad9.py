t = [0, 1, 2, 2, 5, 7, 1, 3, 9, 20]

max_length = 1
i = 0

while i < len(t) -1:
    length = 1
    while i < len(t)-1 and t[i + 1] > t[i]:
        length += 1
        i += 1
    max_length = max(max_length, length)
    i += 1

print(max_length)
