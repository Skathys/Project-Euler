def pyth_triplet():
    for c in range(1,1001):
        for b in range(1,1001):
            if b == c: break
            for a in range(1,1001):
                if a==b:break
                if a+b+c==1000:
                    if a**2+b**2==c**2:
                        product = a*b*c 
                        return product
print(pyth_triplet())
