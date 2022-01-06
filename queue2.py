from typing import Deque


SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1

def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE-1:
        return True
    else :
        return False

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
print(queue) #rear엔 그대로 차있어서 queue가 차있다. 데이터 이동해야한다.