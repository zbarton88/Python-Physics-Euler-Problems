def quad():
    
    def primecheck(n):
        if n == 0:
            return False
        if n == 1:
            return False
        if n == 2:
            return False
        if n == 3:
            return True
        else:
            for i in range(3,n):
                if n%i==0:
                    return False
        return True
    z = 0
    n = 0
    answer = [0,0,0]
    for a in range(-1000,1000):
        for b in range(2,1000):
            if primecheck(b):
                z=0
                n=0
                while primecheck((n**2)+(a*n)+b)==True:
                    n += 1
                    z += 1
                if z > answer[0]: 
                    answer = [z,a,b]
    print (answer)
quad()