import random
dataAry=[ random.randint(10,99) for _ in range(10)]

print('정렬 전 -->', dataAry)

def selecttionSort(ary):
    n=len(ary)
    for cy in range(n-1):
        minIdx=cy
        for i in range(cy+1, n):
            if ary[minIdx]>ary[i]:
                minIdx=i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy] #교환
    return ary           


dataAry=selecttionSort(dataAry)
print('정렬 후 -->', dataAry)