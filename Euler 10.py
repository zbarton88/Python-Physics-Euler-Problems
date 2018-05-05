def sieve():
   
    notprimes = []
    primes = []
    for i in range(2,2000000):
        if i not in notprimes:
            primes.append(i)
            for k in range(i**2,2000000,i):
                notprimes.append(k)
    print(sum(primes))

sieve()