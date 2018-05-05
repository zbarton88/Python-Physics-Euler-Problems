def thirtythree():
    answer = []
    for i in range(10,100):
        for j in range(i+1,100):
            if i%10!=0 and j%10!=0:
                numerator = [int(k) for k in str(i)]
                denom = [int(l) for l in str(j)]
                val2 = 0
                if numerator[0] != numerator[1] and denom[0] != denom[1]:
                    if numerator[0]==denom[0]:
                        val2 = numerator[1]/denom[1]
                    if numerator[1]==denom[1]:
                        val2 = numerator[0]/denom[0]
                    if numerator[1]==denom[0]:
                        val2 = numerator[0]/denom[1]
                    if numerator[0]==denom[1]:
                        val2 = numerator[1]/denom[0]
                    val1 = i/j
                    if val1==val2:
                        answer.append(i)
                        answer.append(j)
    print (answer)
thirtythree()
                
                     
                