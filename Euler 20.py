def problem3(n):
    num = 1
    for i in range(1,n+1):
        num = i * num
    listnum = [int(i) for i in str(num)]
    print(sum(listnum))
problem3(100)