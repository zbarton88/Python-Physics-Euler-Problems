def six():
    n1 = 0
    n2 = 0
    for i in range(1,101):
        n1 += i**2
        n2 += i
    n3 = n2**2
    print (n1-n3)
six()