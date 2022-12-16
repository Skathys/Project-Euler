def smallest_multiple():
    z = 0
    lst = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    while True:
        teilbar = True
        z += 1
        for i in lst:
            if z % i != 0:
                teilbar = False
                break
        if teilbar:
            break
    return z


print(smallest_multiple())
