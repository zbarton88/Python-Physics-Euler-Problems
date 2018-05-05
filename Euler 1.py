import numpy as np

def multiples(n):
    threes = np.sum(range(0,n,3))
    fives = np.sum(range(0,n,5))
    fifteens = np.sum(range(0,n,15))
    print ("the sum of the multiples is",threes + fives - fifteens)
    
multiples(1000)