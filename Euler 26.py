def reciprocal():
    answer=[]
    z=0
    for i in range(1,1000):
        recip = []
        x = 1%i
        y = int(str((10*x)%i)[:1])
        recip.append(x)
        recip.append(y)
        while ((10*y)%i) !=x  :
            y = ((10*y)%i)
            recip.append(y)
            if len(recip)>2000:
                break
        else:
            if len(recip)>z:
                z = len(recip)
                answer = [i]
                   
    print (answer)
reciprocal()
