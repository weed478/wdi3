def czy_only_np(tab):
    for i in tab:
        n = i
        while n > 0:
            n, rem = divmod(n, 10)
            if rem % 2 == 0:
                return False
    return True


print(czy_only_np([11, 931, 7, 31, 17]))
