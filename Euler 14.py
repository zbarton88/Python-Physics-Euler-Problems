def fourteen():
    longest = 0
    answer = 0
    for i in range(2,1000000):
        n=i
        nums = [i]
        while n != 1:
            if n%2==0:
                n = n/2
                nums.append(n)
            else:
                n = 3*n+1
                nums.append(n)
            if len(nums)>longest:
                longest = len(nums)
                answer = i
    print(answer)
fourteen()
