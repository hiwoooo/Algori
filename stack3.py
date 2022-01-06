<<<<<<< HEAD
#최종

SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

def isStackFull():
    global SIZE, stack, top
    if top == SIZE-1 : 
        return True
    else :
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull() : 
        print('스택 꽉 찼다')
        return
    top+=1
    stack[top]=data

def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 : 
        return True
    else : 
        return False

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

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    return stack[top]    


if __name__ =='__main__' :
    select = int(input('1.삽입 2.추출 3.확인 4.종료 중 번호 입력하세요. '))

    while select != 4:
        if select == 1:
            data=input('삽입할 데이터 :')
            push(data)
            print('스택 상태 :', stack)
        elif select == 2 : 
            data=pop()
            print('추출된 데이터는? :', data)
            print('스택 상태 :', stack)
        elif select == 3:
            data=peek()
            print('확인된 데이터 :', data)
            print('스택 상태 :', stack)
        else : 
            print('입력이 잘못되었습니다.')

        select = input('1.삽입 2.추출 3.확인 4.종료 중 번호 입력하세요. ')
    
    print('프로그램 종료')
        


=======
#최종

SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

def isStackFull():
    global SIZE, stack, top
    if top == SIZE-1 : 
        return True
    else :
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull() : 
        print('스택 꽉 찼다')
        return
    top+=1
    stack[top]=data

def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 : 
        return True
    else : 
        return False

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

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비어있다') 
        return None 
    return stack[top]    


if __name__ =='__main__' :
    select = int(input('1.삽입 2.추출 3.확인 4.종료 중 번호 입력하세요. '))

    while select != 4:
        if select == 1:
            data=input('삽입할 데이터 :')
            push(data)
            print('스택 상태 :', stack)
        elif select == 2 : 
            data=pop()
            print('추출된 데이터는? :', data)
            print('스택 상태 :', stack)
        elif select == 3:
            data=peek()
            print('확인된 데이터 :', data)
            print('스택 상태 :', stack)
        else : 
            print('입력이 잘못되었습니다.')

        select = input('1.삽입 2.추출 3.확인 4.종료 중 번호 입력하세요. ')
    
    print('프로그램 종료')
        


>>>>>>> abc03d1abb22258af78b4458c71616b7883cf05a
