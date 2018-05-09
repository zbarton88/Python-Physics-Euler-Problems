def problem15():
    n = 1
    j = 1
    for i in range(1,21):
        n = n*i
    for i in range(1,41):
        j = j*i
    answer = (j/n)/n
    print (answer)
problem15()