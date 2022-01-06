#큐의 일반 구현

SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1

#꽉 안차있으면 front의 위치 확인해서 -1이 아닐 경우, 앞으로 땡기기 추가
def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE-1: #꼬리가 끝까지 안차있다면 
        return False
    elif (rear == SIZE-1) and (front == -1): #front부터 rear까지 큐 사이즈에 꽉 차있는지
        return True
    else : #
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear-=1
        return False

#이렇게 추가된 기능은 enQueue에서 써먹힌다. 
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() : 
        print('큐 꽉')
        return 
    rear+=1
    queue[rear]=data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front==rear:
        print('큐 비어있음')
        return True
    else : 
        return False

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 비어있음')
        return None
    front += 1
    data=queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 비어있음')
        return None
    return queue[front+1]


enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print(queue)
print('입장손님 :',deQueue())
print('입장손님 :',deQueue())
print(queue)
enQueue('혜우')
print(queue) 
enQueue('나딘')
print(queue)