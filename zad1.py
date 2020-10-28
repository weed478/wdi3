n = int(input("Num: "))
base = int(input("Base: "))

print("Num:", n, " | Converted:", end=" ")


# tu jest potencjał
def convert_num(n, base):
    if n > 1:
        convert_num(n // base, base)
    rem = n % base
    if rem >= 10:
        rem = chr(rem + 55)
    print(rem, end='')


# a to działa
output = ""
while n > 0:
    tmp = n % base
    if tmp >= 10:
        tmp = chr(tmp + 55)
    output = str(tmp) + output
    n //= base

print(output)
