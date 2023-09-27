import sys
from math import sqrt
input = sys.stdin.readline

def func(n): #소수 판별 함수
    result = 0
    if n == 1:
        return result
    for j in range(2,int(sqrt(n)) + 1): #i-1 까지임
        if n % j == 0:
            break
    else:
        result += 1
    return result
  
while 1:
    b = int(input())
    if b == 0:
      exit()
    num1, num2 = 2, b-2

    while num1 > 0: #골드바흐가 맞아버려서 틀리지가 않아버려이~~
        if func(num1) and func(num2):
            print("{0} = {1} + {2}".format(b,num1,num2))
            break
        else:
            num1 += 1
            num2 -= 1
'''
짝수 던져주면 홀수소수 + 홀수소수 로 가능
(6 ≤ n ≤ 1000000)
0입력 끝
b-a가 가장 큰 것을 출력
a,b 홀수
"Goldbach's conjecture is wrong." 이거 왜 써놓은 겨 ㅋㅋ
예제 입력 1 
8
20
42
0
예제 출력 1 
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
'''