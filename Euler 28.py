import numpy as np
def spirals():
    length = 1001      
    nums = np.arange(1,(length**2)+1)
    vals = []
    n=1  
    interval = 0        
    while n < (length**2+1):
        interval += 2
        for i in range(0,4) :
            if  n < (length**2+1):
                vals.append(nums[n-1])
                n += interval
    print (sum(vals))
spirals()