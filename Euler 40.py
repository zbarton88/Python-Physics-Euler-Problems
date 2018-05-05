def forty():
    n = ''
    while len(n)< 1000000:
        for i in range(0,1000000):
            n = n+str(i)
    answer = int(n[1])*int(n[10])*int(n[100])*int(n[1000])*int(n[10000])*int(n[100000])*int(n[1000000])
    print (answer)
forty()        