import numpy as np

def factorialsum(n):
    nums = [int(d) for d in str(n)]
    answer = 0
    for i in range(0,len(nums)):
       n = np.math.factorial(nums[i])
            
       answer += n
    return answer

factorialsum(33)

def problem34():
    n = 0
    for i in range(3,100000):
        if factorialsum(i)==i:
            n += i
    print(n)
problem34()