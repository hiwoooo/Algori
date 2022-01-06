def printStar(num):
    if num>0:
        printStar(num-1)
        print('*'*num)

print(printStar(5))