def sieve():
   
    notprimes = []
    primes = []
    n = []
    length = 0
    for i in range(2,1000000):
        if i not in notprimes:
            primes.append(i)
            for k in range(i**2,1000000,i):
                notprimes.append(k)
    for i in range(0,len(primes)):
        n=[]
        for j in range(0,i):
           n.append(primes[j])
        if primes[i]==sum(n) and len(n)>length:
            length = len(n)
            answer = primes[i]
    print(answer)



sieve()