import random

tab = []
for i in range(100):
    tab.append(random.randrange(1, 100, 2))
# tab = [2, 4, 6, 0, 9, 2, 1, 1, 2, 3, 4, 5, 7, 5, 4, 6, 1, 4, 7, 9]
max_length_ascend = 1
max_length_desc = 1

i = 0

while i < len(tab) - 1:
    length = 1
    difference = tab[i + 1] - tab[i]
    while i < len(tab) - 1 and tab[i + 1] - tab[i] == difference:
        length += 1
        i += 1
    if difference > 0:
        max_length_ascend = max(max_length_ascend, length)
    else:
        max_length_desc = max(max_length_desc, length)

print(max_length_ascend - max_length_desc)
