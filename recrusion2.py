def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('##반지 넣기##')
        return
    openBox()
    print('상자 닫기')
    return

#재귀함수 호출해서 if문을 만족해서 return이 되면 직전단계의 print 명령으로 넘어간다.
#마지막 return은 다시 직전단계의 print 명령으로 넘어간다.


count=3
openBox()