from datetime import date
def problem19():
    n = 0
    for i in range(1901,2001):
        for j in range(1,13):
            day = date(i,j,1).weekday()
            if day == 6:
                n += 1
    print (n)
problem19()
            