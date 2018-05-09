def problem31():
    nums = [1,2,5,10,20,50,100,200]
    answer = [1] + [0]*200
    
    for i in nums:
        for j in range(i,201):
            answer[j] += answer[j-i]
    print(answer[200])
problem31()