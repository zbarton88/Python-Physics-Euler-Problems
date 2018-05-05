def sieve(n):
    answer = []
    notprimes = []
    primes = []
    for i in range(2,10000):
        if i not in notprimes:
            primes.append(i)
            for k in range(i**2,10000,i):
                notprimes.append(k)
    for i in range(3,len(primes)):
        n1 = primes[i]
        n2 = primes[i]+3330
        n3 = primes[i]+6660
        if n2 in primes and n3 in primes:
            str1 = str(n1)
            str2 = str(n2)
            str3 = str(n3)
            if len(str1)==len(str2)==len(str3) and sorted(str1)==sorted(str2)==sorted(str3):
                answer.append(n1)
                answer.append(n2)
                answer.append(n3)
    print(answer)



sieve(100)