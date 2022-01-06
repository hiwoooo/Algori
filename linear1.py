
katok=[]

def add_data(friend):
    katok.append(None)
    kLen=len(katok) #데이터가 많을 경우 항상 데이터의 길이를 파악해야함.
    katok[kLen-1]=friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
#print(katok)

add_data('모모')
#print(katok)

#새로운 데이터가 중간에 들어올때
#katok.append(None)
#katok[6]=katok[5]
#katok[5]=None #자리비움
#katok[5]=katok[4]
#katok[4]=None
#katok[4]=katok[3]
#katok[3]='미나'
#print(katok) 
#너무 길고 비효율. 함수로 바꾸자

def insert_data(position, friend): #katok[position]에 데이터 추가
    katok.append(None) #데이터 추가, 배열 확장
    kLen=len(katok) #확장된 배열의 길이
    for i in range(kLen-1, position,-1): #마지막 원소자리부터 역행으로 
        katok[i]=katok[i-1] #뒤로 자리이동
        katok[i-1]=None #복사된것은 비움.
    katok[position] = friend

insert_data(3, '미나')
#print(katok)

#순위 삭제, 리스트는 빈칸 허용X 뒷사람들 앞으로 끌어와야함

def delete_data(position):
    katok[position]=None
    kLen=len(katok) 
    for i in range(position+1, kLen,1): #비워진 다음차례부터 앞으로 땡기기
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[kLen-1]) #전체 길이에서 마지막원소자리 삭제

delete_data(4)
#print(katok)
    

#실습
#1. 추가  2.삽입    3.삭제     4.종료

if __name__=='__main__':
    select=int(input("1.추가 2.삽입 3.삭제 4.종료" ))

    while (select != 4):
        

        if select==1:
            data=input("추가할 데이터 : ")
            add_data(data)
            print(katok)
            

        elif select==2:
            pos=int(input("삽입할 위치 : " ))
            data=input("추가할 데이터 : " )
            insert_data(pos, data)
            print(katok)
        elif select==3:
            pos=int(input("삭제할 위치 : "))
            delete_data(pos)
            print(katok)
        