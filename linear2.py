class Node(): #Node이름의 클래스
    def __init__(self): #노드생성. 그냥 이렇게쓴다.
        self.data=None
        self.link=None


node1=Node()
node1.data='다현'
node2=Node()
node2.data='정연'
node1.link=node2 #노드1과 노드2 연결
node3=Node()
node3.data='쯔위'
node2.link=node3 
node4=Node()
node4.data='사나'
node3.link=node4 
node5=Node()
node5.data='지효'
node4.link=node5 
#다현을 시작으로 노드 연결
#쯔위를 출력하고싶다.
#print(node1.link.link.data, end=' ')

#삽입
newNode=Node()
newNode.data='재남'
newNode.link=node2.link #삽입위치확인, node2.link는 세번째 자리
node2.link=newNode

#삭제
#node2.link=node3.link
#del(node3)


current=node1
print(current.data, end=' ')
while current.link != None:
    current=current.link
    print(current.data, end=' ')
