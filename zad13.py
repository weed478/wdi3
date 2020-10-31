from random import randint


def random_tab(N):
    return [randint(100, 999) for _ in range(N)]


tab = random_tab(1000)

# tab = [2, 9, 3, 1, 7, 11, 9, 6, 11, 7, 1, 3, 9, 9, 7, 7, 1, 3, 9, 9, 12, 15, 67, 674, 8, 587, 546347, 4367, 45734,
#        44543, 4535, 453543, 5354353, 5345345, 345353, 636, 56343634, 65363, 635636, 36363, 536363563, 635]

# tab = [0, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]
# tab = [0, 1, 2, 3, 4, 3, 2, 1]

max_length = 0
length = 0
left = 0
while left < len(tab):
    right = len(tab) - 1
    while right >= 0:
        if tab[left] == tab[right]:
            check_left = left
            check_right = right
            length = 0
            while check_left < len(tab) and check_right >= 0:
                if tab[check_left] == tab[check_right]:
                    length += 1
                else:
                    break
                check_left += 1
                check_right -= 1
            if length > max_length:
                max_length = length
            right -= length - 1
        right -= 1
    left += 1
print(max_length)
