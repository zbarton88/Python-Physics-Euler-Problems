def factorssum(n):
    fact = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            fact.append(i)
    return sum(fact)
    
factorssum(220)
answer = []
for i in range(1,10000):
    x1 = factorssum(i)
    x2 = factorssum(x1)
    if x2==i and x1!=i:
        answer.append(i)
print(sum(answer))
        