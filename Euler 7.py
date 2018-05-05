def sieve(n):
   
    notprimes = []
    primes = []
    for i in range(2,110000):
        if i not in notprimes:
            primes.append(i)
            for k in range(i**2,110000,i):
                notprimes.append(k)
    print("the 10001 prime number is:",primes[10000])



sieve(100)
    