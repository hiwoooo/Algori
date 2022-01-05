#stack=[None,None,None,None,None] 의 다른표현
SIZE=5
stack=[None for _ in range(SIZE)]
top=-1

#푸시
top+=1
stack[top]='커피' 
top+=1
stack[top]='녹차'
top+=1
stack[top]='꿀물'
#print(stack)

#pop
data=stack[top]
stack[top]=None
top-=1
#print('팝->',data)
data=stack[top]
stack[top]=None
top-=1
data=stack[top]
stack[top]=None
top-=1
print(stack) #전부다 팝

