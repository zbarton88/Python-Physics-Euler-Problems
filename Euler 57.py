def prob57():
    denom = 2
    numer = 3
    n = 0
    for i in range(0,1000):
        numer += 2*denom
        denom = numer-denom
        if len(str(numer))>len(str(denom)):
            n += 1
    print(n)
prob57()
    
    