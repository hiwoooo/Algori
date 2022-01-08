#N제곱 계산하기
#어려워.....

def calcul(n,m):
    if n != 0 and m>=0:
        if m==0:
            return n**m
        else : 
            ##참고
            return n*calcul(n,m-1)

#print!!!    
print(calcul(2,4))