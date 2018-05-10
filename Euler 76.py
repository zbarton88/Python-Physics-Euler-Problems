def problem76(n):

    num = n
    nums = range(1, n)
    ways = [1] + [0]*n
    
    for i in nums:
        for j in range(i, n+1):
            ways[j] += ways[j-i]
    print(ways[n])
problem76(100)