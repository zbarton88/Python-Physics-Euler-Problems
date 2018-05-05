def problem4():
    listn = [1,1]
    i = 1
    number = [0]
    while len(number) <1000:
        i+=1
        num = listn[i-1]+listn[i-2]
        listn.append(num)
        number = [int(j) for j in str(max(listn))]
    print (len(listn))
problem4()