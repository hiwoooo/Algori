#랜덤하게 생성한 배열의 합계

import random

N=int(input())
Ary=[random.randint(1,500) for _ in range(N)]

def ranSum(arr,n):
  if n<=0 :
    return arr[0]
 # else :
  return (arr[n]+ranSum(arr,n-1))
 

print(Ary)
# print(ranSum(Ary,N)) --> 수정,배열 자리 확인하기!!!
print(ranSum(Ary,N-1))
