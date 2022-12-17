from math import isqrt
from time import perf_counter as pfc

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


start = pfc()
s = sum(n for n in range(2, 2_000_000) if is_prime(n))
print(pfc() - start)
print(s)
