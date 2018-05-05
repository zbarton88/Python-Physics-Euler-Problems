import numpy as np
from itertools import permutations 

nums = list(map("".join,permutations('1234567')))
array = []
answer = []
for i in range(2,len(nums)):
    array.append(int(nums[i]))
    for j in range(2,int(np.sqrt(i))):
        while i%j==0:
            continue
        if j == int(np.sqrt(i)):
            answer.append(i)
        else:
            break
        

print(max(answer))


    
    

                    
            
    