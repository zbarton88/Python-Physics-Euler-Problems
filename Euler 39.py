import numpy as np
def prob39(n):
    num = 0
    biggest = 0
    for i in range(2,n+1,2):
        answer = 0
        for k in range(1,i+1):
            for j in range(k,i+1):
                
                c = np.sqrt(j**2+k**2)
            
                if c == i-k-j:
                    answer += 1
                    if answer > biggest:
                        num=i
                        biggest = answer
    print (num,biggest)                
prob39(1000)