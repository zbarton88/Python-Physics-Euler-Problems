
def fiftytwo():
    i = 1
    while True:
        i+=1
        a = str(i)
        b = 2*i
        c = 3*i
        d = 4*i 
        e = 5*i 
        f = 6*i
        if sorted(str(i))==sorted(str(b))==sorted(str(c))==sorted(str(d))==sorted(str(e))==sorted(str(f)):
            answer = i
            break
    print (answer)
fiftytwo()
    