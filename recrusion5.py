def Countdown(num):
    
    if num == 0:
        print('발사') 
        
    else :
        print(num)
        Countdown(num-1)

print(Countdown(5))

#나 왜 none까지 나오지?..
