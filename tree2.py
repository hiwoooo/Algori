memory=[]
root=None
nameAry=['블랙핑크','레드벨벳','에이핑크','걸스데이','마마무','트와이스']

class TreeNode():
    def __init__(self) :
        self.data=None
        self.left=None
        self.right=None

node=TreeNode()
node.data=nameAry[0]
root=node
memory.append(node)


for name in nameAry[1:] : #레드벨벳부터
    node=TreeNode()
    node.data=name

    current=root
    while True : 
        
        if name<current.data:
            current.left=node
            if current.left == None:
                current.left==node
                break
            current=current.left    
        else : 
            if current.right==None:
                current.right= node
                break
            current=current.right

    memory.append(node)

#print('이진 탐색 트리 구성 완료')


#이진 탐색 트리 활용 (검색)
findname='마마무'
current=root
while True:
    if findname == current.data :
        print(findname, '찾음')
        break
    elif findname < current.data :
        if current.left == None : #왼쪽노드 더이상 없으면 끝. 자료 없음
            print('없음')
            break
        current = current.left
    else :
        if current.right == None : #오른쪽 노드 더이상 없으면 끝. 자료 없음
            print('없음')
            break
        current=current.right

print('종료')
            
