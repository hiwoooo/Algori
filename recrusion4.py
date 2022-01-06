#팩토리얼 구하기
def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

print('5!=', factorial(5))