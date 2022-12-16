a, b = 1, 0
lst = []
while True:
    a, b = a + b, a
    if a > 4_000_000:
        break
    if a % 2 == 0:
        lst.append(a)

print(sum(lst))
