def problem29():
    thing = []
    for i in range(2,101):
        for j in range(2,101):
            if i**j not in thing:
                thing.append(i**j)
    print (len(thing))
problem29()