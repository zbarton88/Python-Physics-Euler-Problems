def problem63():
    count = 0
    for i in range(1,10000):
        for j in range(1,100):
            num = i**j
            if len(str(num))==j:
                count += 1
    print(count)
problem63()
