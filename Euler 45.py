

def fortyfive():
    i = 1
    t = []
    p = []
    h = []
    for i in range(2,1000000):
        t.append(i*(i+1)/2)
        p.append(i*(3*i-1)/2)
        h.append(i*(2*i-1))
    tp = list(set(t).intersection(p))
    num = list(set(tp).intersection(h))
    print(num)
fortyfive()
        
