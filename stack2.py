<<<<<<< HEAD
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

#꽉 차있는지 확인. 차있으면 푸시 안함
def isStackFull(): #많이들 이렇게 쓴다. is stack full?
    global SIZE, stack, top
    if top == SIZE-1 : 
        return True
    else :
        return False

#푸시
def push(data):
    global SIZE, stack, top
    if isStackFull() : #true이면 실행
        print('스택 꽉 찼다')
        return
    top+=1
    stack[top]=data

#pop전에 비어있는지 확인
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 : 
        return True
    else : 
        return False

#POP
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    else : 
        data=stack[top]
        stack[top]=None
        top-=1
        return data

#top확인하고싶어
def peak():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    return stack[top]    




#stack=['커피','녹차','꿀물','콜라','환타']
#top=4
#print(isStackFull())

#stack=['커피','녹차','꿀물','콜라',None]
#top=3
#push('보리차')
#print(stack)
#push('사이다')
#print(stack)

stack = ['커피', None, None, None, None]
top = 0
print('다음나올 데이터는? : ', peak() )
print(pop()) #pop하면 top의 '커피'가 데이터로 저장,출력
=======
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

#꽉 차있는지 확인. 차있으면 푸시 안함
def isStackFull(): #많이들 이렇게 쓴다. is stack full?
    global SIZE, stack, top
    if top == SIZE-1 : 
        return True
    else :
        return False

#푸시
def push(data):
    global SIZE, stack, top
    if isStackFull() : #true이면 실행
        print('스택 꽉 찼다')
        return
    top+=1
    stack[top]=data

#pop전에 비어있는지 확인
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 : 
        return True
    else : 
        return False

#POP
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    else : 
        data=stack[top]
        stack[top]=None
        top-=1
        return data

#top확인하고싶어
def peak():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    return stack[top]    




#stack=['커피','녹차','꿀물','콜라','환타']
#top=4
#print(isStackFull())

#stack=['커피','녹차','꿀물','콜라',None]
#top=3
#push('보리차')
#print(stack)
#push('사이다')
#print(stack)

stack = ['커피', None, None, None, None]
top = 0
print('다음나올 데이터는? : ', peak() )
print(pop()) #pop하면 top의 '커피'가 데이터로 저장,출력
>>>>>>> abc03d1abb22258af78b4458c71616b7883cf05a
print(pop()) #비어있는 스택은 pop할 수 없다.