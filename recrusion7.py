#구구단 출력하기

def gugudan(num):
    if num>0:
        gugudan(num-1)
        print((' %d 단')%(num))
        for i in range(2,10):            
            print(('%d X %d = %d') %(num,i,num*i))

gugudan(5)

