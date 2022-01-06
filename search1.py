import random
dataAry=[ random.randint(10,99) for _ in range(10)]
findData=dataAry[random.randint(0,19)]

print('배열-->', dataAry)

def seqSearch(ary, fData):
    pos=-1
    for i in range(len(ary)):
        if ary[i]== fData:
            pos=i
            break
    return pos


position=seqSearch(dataAry, findData)
if position== -1:
    print(findData, '없음')
else :
    print(findData, ',', position,'위치에 있음')