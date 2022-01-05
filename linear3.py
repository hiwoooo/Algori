class Node(): #Node이름의 클래스
    def __init__(self): 
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    print(current.data, end=' ')
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print()

#삽입
def insertNode(findData,insertData):
    global memory, head,current, pre
    #첫노드에 넣을때
    if head.data==findData : 
        node=Node()
        node.data=insertData
        node.link=head
        head=node
        return
    
    #중간노드 앞에 삽입
    current=head
    while current.link != None:
        pre=current
        current=current.link
        if current.data == findData : 
            node=Node()
            node.data=insertData
            node.link=current
            pre.link=node
            return
    #없는 데이터 앞에 추가 = 마지막에 추가
    node=Node()
    node.data=insertData
    current.link=node
    return

#삭제
def deleteNode(deleteData):
    global memory, head,current, pre
    #헤드를 삭제할때
    if head.data==deleteData:
        current=head
        head=head.link
        del(current)
        return

    #중간노드 삭제할때
    current=head
    while current.link != None:
        pre=current
        current=current.link
        if current.data == deleteData : 
            pre.link=current.link
            del(current)
            return

#검색
def findNode(findData):
    global memory, head,current, pre
    current=head
    if current.data==findData:
        return current
    while current.link != None:
        current=current.link
        if current.data==findData:
            return current
    return Node()



        
#작업할 원소를 current, current의 바로 앞 원소는 pre
#pre.link==current 이므로 작업 가능.

memory=[]
head,current,pre=None,None,None
dataArray=['다현','정연','쯔위','사나','지효']

#첫 노드 생성
node=Node() 
node.data=dataArray[0]
head=node #헤더 중요, 첫노드
memory.append(node)

for data in dataArray[1:]: #두번째원소부터 마지막까지
    pre=node
    node=Node()
    node.data=data
    pre.link=node
    memory.append(node)

#printNodes(head) #헤드에 줄줄이 노드 연결어있다.

insertNode('다현', '화사')
#printNodes(head)

insertNode('쯔위','솔라')
#printNodes(head)

insertNode('재남', '문별')
#printNodes(head)

deleteNode('화사')
deleteNode('사나')
deleteNode('재남') #없는 데이터는 원본 그대로 유지
printNodes(head)

fNode=findNode('쯔위')
print(fNode.data)
fNode=findNode('재남')
print(fNode.data)