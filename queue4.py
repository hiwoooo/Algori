#원형 큐, front가 0에서 시작

SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=0

#rear가 front바로 앞일때
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1)%SIZE == front:
        return True
    else :
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() : 
        print('큐 꽉')
        return 
    rear= (rear+1)%SIZE
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
    front = (front+1)%SIZE
    data=queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 비어있음')
        return None
    return queue[(front+1)%SIZE]


enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print(queue) #원형큐는 한자리 비워져있다
print('입장할 손님 :', deQueue())
print('입장할 손님 :', deQueue())
enQueue('혜우')
print(queue) 
#원형이라 휘인의 뒷자리=front
