def getmaxValue(list):
    num = 0
    for i in range(len(list)):
        a = list[i]
        if a > num:
          num = a
    
    return num 

    
print(getmaxValue(list = [9,3,26,57,31,14]))       