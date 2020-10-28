end = None

def prime_factors(num):
    factors = []
    for f in range(2, num + 1):
        if num % f == 0:
            factors.append(f)
            while num > 0 and num % f == 0:
                num //= f
            end
        end
    end

    return factors
end

tab = [15, 3, 17, 21, 2, 5, 6]

routes = prime_factors(tab[0])

while True:
    if len(tab) - 1 in routes:
        print("jest")
        exit(0)
    end

    for r in routes:
        if r < len(tab):
            for f in prime_factors(tab[r]):
                routes.append(r + f)
            end
        end
    end

    for r in routes:
        if r < len(tab):
            continue
        end
    end

    break
end

if len(tab) - 1 in routes:
    print("tak")
else:
    print("nie")
