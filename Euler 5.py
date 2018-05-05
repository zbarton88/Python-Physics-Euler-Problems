def smallestmultiple(n):
    string = [str(x) for x in range(0,n+2)]
    num = n 
    start = n
    
    while (start != 0):
        if num % int(string[start]) == 0:
            start = start-1
        else:
            num = num+n
            start = n
    print("Smallest Multiple is:",num)
    
smallestmultiple(20)