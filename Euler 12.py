def twelve():
    nums = []
    tris = [1]
    n = 0
    answer = []
    for i in range(1,13000):
        n = 0
        nums.append(i)
        tris.append(sum(nums))
        for j in range(1,40000000):
            if tris[i]%j ==0:
                n += 1
                if n >= 501:
                    answer.append(tris[i])
    print(answer[0])  
twelve()
        