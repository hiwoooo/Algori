import random
testAry=[ random.randint(1,99) for _ in range(20)]

#최솟값구하기
def findMinIndex(ary):
    minIdx=0
    for i in range(1,len(ary)):
        if ary[minIdx] > ary[i] :
            minIdx=i

    return minIdx

print(testAry)
minPos=findMinIndex(testAry)
print('최솟값-->', testAry[minPos])

