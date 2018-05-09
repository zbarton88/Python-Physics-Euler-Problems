
def problem92():
    answer = []
    for k in range(1,10000000):
        num = k
        while True:
            work = num 
            num = 0 
            for j in str(work):
                num += int(j)**2
            if num == 89:
                    answer.append(k)
                    break
            if num == 1:
                    break
            
    print(len(answer))
problem92()
            