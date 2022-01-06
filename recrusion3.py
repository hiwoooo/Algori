#1부터 자기자신까지의 합
def addNum(num):
    if num<=1:
        return 1
    return num+addNum(num-1)

print(addNum(10))