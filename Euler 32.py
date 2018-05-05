

def pandigital():
    nums = set('123456789')
    vals = set()
    for i in range(10,100):
        for k in range(100,1000):
            x = i*k 
            
            check = str(x)+str(i)+str(k)
            
            if len(check) == 9 and set(check)==nums:
                vals.add(x)
    for i in range(1,10):
        for k in range(1000,10000):
            x = i*k 
            check = str(x)+str(i)+str(k)
        
            
            if len(check) == 9 and set(check)==nums:
                vals.add(x)
    print(vals,sum(vals))
pandigital()