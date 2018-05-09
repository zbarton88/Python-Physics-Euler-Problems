
def problem55():
    nums = []
    for i in range(10,10000):
        nums.append(i)
    for i in range(10,10000):
        count = 0
        num = i
        while count<50:
            reverse = str(num)
            num = num + int(reverse[::-1])
            check = str(num)
            
            if check==check[::-1]:
                nums.remove(i)
                break
            count += 1
    print(len(nums))
problem55()
