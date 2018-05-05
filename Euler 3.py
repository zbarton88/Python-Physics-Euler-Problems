def factorlist(n):
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
string = list(filter(factorlist, range(1,1000)))

def smallestfactor(n):
    
    num = int(n**0.5)
    primes = list(filter(factorlist, range(2,num)))
    check = [n % x for x in primes][::-1].index(0)
    answer = primes[len(primes)-check-1]
    alt = int(n / answer)
    if n % answer == 0 and list(filter(factorlist, range(alt-1, alt+1))).count(n / answer) == 1:
        newanswer = int( n / answer)
        print ("Smallest Prime Factor is:", newanswer)
    else:
        print ("Smallest Prime Factor is:", answer)
smallestfactor(600851475143)