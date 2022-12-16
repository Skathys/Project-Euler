def primes(n):

    i = 0
    zahl = 3
    primes = [2,3]

    while True:
        zahl += 1
        is_prime = True
        for digit in range(2, zahl):
            if zahl % digit == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(zahl)
            i += 1
        if i == n-2:
            break
    return max(primes)

print(primes(10001))
