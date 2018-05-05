def fib():
    nums = [1,2]
    answer = 0
    n = 1
    while max(nums)< 4000000:
        nums.append(nums[n]+nums[n-1])
        n += 1
    for i in range(1,len(nums)):
        if nums[i]%2 == 0:
            answer += nums[i]
    print (answer)
fib()