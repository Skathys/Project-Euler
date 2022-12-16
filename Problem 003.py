def prime_checker(number):
    if number == 1:
        is_prime = False
    else:
        is_prime = True

    for digit in range(2, number):
        if number % digit == 0:
            is_prime = False
            break

    return is_prime


def list_primes(anzahl_primes):
    i = 1
    lst_primes = []

    while True:
        i += 1
        if anzahl_primes == len(lst_primes):
            break
        if prime_checker(i):
            lst_primes.append(i)

    return lst_primes


def groeßter_primfaktor(n, liste_anzahl_primes):
    primfaktoren = []
    for prime in list_primes(liste_anzahl_primes):
        while n % prime == 0:
            n = n // prime
            primfaktoren.append(prime)
            if n < prime:
                break
    return primfaktoren


print(max(groeßter_primfaktor(600_851_475_143, 1000)))
