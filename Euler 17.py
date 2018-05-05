def fifteen():
    a = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,9,8]
    b = [0,0,6,6,5,5,5,7,6,6]
    longest = 1
    for i in range(1,1000):
        num = i
        string = [int(j) for j in str(num)]
        if i<20:
            answer = a[i]
        if 20<=i<=99:
            answer = a[string[1]]
            answer += b[string[0]]
        if i>=100:
            if 10<int(str(string[1])+str(string[2]))<20:
                answer = a[int(str(string[1])+str(string[2]))] +a[string[0]] + 3 + 7
            else:
                answer = a[string[2]]+b[string[1]]+a[string[0]]+3+7
        longest += answer
    print(longest)
fifteen()