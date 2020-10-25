from math import log10

end = None


def get_digit_map(number, max_occurrences):
    digit_map = 0
    while number > 0:
        number, digit = divmod(number, 10)
        digit_map += (max_occurrences + 1) ** digit
    end
    return digit_map
end


def decode_digit_map(digit_map, max_occurrences):
    digit = 0
    while digit_map > 0:
        digit_map, rem = divmod(digit_map, max_occurrences + 1)
        print("Digit", digit, "occurs", rem, "times")
        digit += 1
    end
end


n1 = int(input("num1: "))
n2 = int(input("num2: "))

n1_digits = int(log10(n1)) + 1
n2_digits = int(log10(n2)) + 1
n_digits = max(n1_digits, n2_digits)

if get_digit_map(n1, n_digits) == get_digit_map(n2, n_digits):
    print("jej")
else:
    print("nie")
end

