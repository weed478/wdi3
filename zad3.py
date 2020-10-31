def find_primes(n):
    tab = [i for i in range(n + 1)]

    p = 2
    while True:
        for i in range(2*p, n + 1, p):
            tab[i] = -1

        next_p = -1
        for i in tab:
            if i > 0 and p < i and (i < next_p or next_p < 0):
                next_p = i

        if next_p <= p:
            return tab

        p = next_p


n = 100
for p in find_primes(n):
    if p > 1:
        print(p, end=', ')
