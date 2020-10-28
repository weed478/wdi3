t = [0, -3, -2, -1, 0, 1, 2, 4, 8, 16, 32, 8, 2, 5, 7, 1, 3, 9, 21]

max_length = 1
i = 0

while i < len(t) - 1:
    length = 1
    if t[i] != 0:
        q = t[i + 1] / t[i]
        while i < len(t) - 1 and t[i] != 0 and t[i + 1] / t[i] == q:
            length += 1
            i += 1
        max_length = max(max_length, length)
    else:
        i += 1

print(max_length)
