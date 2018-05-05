def fifths():
    n = 400000
    vals =[]
    for i in range(2,n):
        x = [int(kk)**5 for kk in str(i)]
        if sum(x) == i:
            vals.append(i)
    print(sum(vals))
fifths()