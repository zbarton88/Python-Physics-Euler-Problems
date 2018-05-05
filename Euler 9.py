def tripple():

    for x in range(1,1000,1):
        for y in range(x+1,1000,1):
            z = 1000-x-y
            if x**2+y**2==z**2:
                    print("Product of Pythagorean Tripple is:",x*y*z)
tripple ()