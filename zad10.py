t = [-3, -2, -1, 0, 1, 2, 4, 6, 8, 2, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 17]

max_length = 1
i = 0

while i < len(t) - 1:
    length = 1
    difference = t[i+1] - t[i]
    while i < len(t) - 1 and t[i + 1] - t[i] == difference:
        length += 1
        i += 1
    max_length = max(max_length, length)

print(max_length)
