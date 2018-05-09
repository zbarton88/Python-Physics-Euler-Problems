def factorssum(n):
    fact = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            fact.append(i)
    return sum(fact)
    
factorssum(25)


def problem23():
    abund = []
    sums = []
    alls = range(0,28124)
    for i in range(0,28124):
        if factorssum(i)>i:
            abund.append(i)
    for i in range(0,len(abund)):
        for j in range(i,len(abund)):
            x = abund[i]+abund[j]
            sums.append(x)
    print(sum(list(set(alls)-set(sums))))
    
problem23()
            
    