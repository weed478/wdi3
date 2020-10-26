def sito(n):
    tab = [True] * (n - 1)
    count = 0

    for i in range(2, int(n ** 0.5) + 1):
        if tab[i - 2]:
            j = i - 2 + i
            while j < n - 1:
                if tab[j]:
                    tab[j] = False
                    count += 1
                j += i

    for i in range(2, n + 1):
        if tab[i - 2]:
            tab[i - 2] = i

    for i in range(count):
        tab.remove(False)

    print(tab)


sito(25)
