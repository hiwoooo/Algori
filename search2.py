import random
dataAry=[ random.randint(1,999) for _ in range(20)]
findData=dataAry[random.randint(1,49)]
dataAry.sort()


def binSearch(ary, fData):
    pos = -1
    start=0
    end=len(ary)-1
    while start<=end:
        mid=(start+end)//2
        if fData==ary[mid] : 
            return mid
        elif fData > ary[mid]:
            start=mid+1
        else :
            end=mid-1
    return pos 


print('배열-->', dataAry)
position=binSearch(dataAry, findData)
if position== -1:
    print(findData, '없음')
else :
    print(findData, ',', position,'위치에 있음')