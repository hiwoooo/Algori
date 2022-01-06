SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1

#enQueue
rear+=1
queue[rear]='화사'
rear+=1
queue[rear]='솔라'
rear+=1
queue[rear]='문별'
#print('출구<--', queue, '<--입구')

#deQueue
front+=1
data=queue[front]
queue[front]=None
print('첫번째 호출:',data)
front+=1
data=queue[front]
queue[front]=None
print('두번째 호출:',data)
front+=1
data=queue[front]
queue[front]=None
print('세번째 호출:',data)
print('출구<--', queue, '<--입구')
