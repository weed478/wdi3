a = 10 # ktory max
num = [0] * (a + 1)

while True:

    while True:
        num[-1] = int(input("> "))
        if num[-1] >= 0:
            break
        print("Liczba musi byc naturalna")

    if num[-1] == 0:
        break

    for i in range(len(num) - 2, -1, -1):
        if num[i] > num[i + 1]:
            break
        elif num[i] == num[i + 1]:
            num.append(0)
            break
        else:
            num[i], num[i + 1] = num[i + 1], num[i]

    print(num)

if num[-2] == 0:
    print("nope")
else:
    print(num[-2])
