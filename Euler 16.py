import numpy as np

def problem2(n):
    num = 2**n
    listnum = [int(i) for i in str(num)]
    print(np.sum(listnum))
problem2(1000)