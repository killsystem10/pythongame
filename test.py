import time
import random
list=[0,0,1,2,3,4,5,6,7,8,9]
print("너의 숫자 입력 실력을 알아본다!")
print("랜덤 16개의 숫자를 10번 입력하라")
temp=input("엔터 시 시작")
for i in range(1,11):
    print(i, "번째 문제")
    for temp in range(16):
        word=random.randint(0,9)
        print(word)
