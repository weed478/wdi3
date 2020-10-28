def czy_np(tab):
    for i in tab:
        n = i
        while n > 0:
            n, rem = divmod(n, 10)
            if rem % 2 == 1:
                break
        else:
            return False
    return True


print(czy_np([12, 431, 7, 61, 462]))
