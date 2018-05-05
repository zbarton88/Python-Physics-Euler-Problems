def fiftysix():
    answer = 0
    for i in range(1,101):
        number = 0
        num = 0
        for j in range(1,101):
            number = i**j
            num = sum(int(k) for k in str(number))
            if answer<num:
                answer = num
    print (answer)
fiftysix()
            