def sito(n):
    tab = [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if tab[i - 2]:
            j = i - 2 + i
            while j < n - 1:
                if tab[j]:
                    tab[j] = False
                j += i

    output = []
    for i in range(2, n + 1):
        if tab[i - 2]:
            output.append(i)

    print(output)


sito(100)
