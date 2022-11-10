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

a = int(input())

for i in range(a):
    b = int(input())
    
    num1, num2 = b//2, b//2
    while num1 > 0:
        if func(num1) and func(num2):
            print(num1, num2)
            break
        else:
            num1 -= 1
            num2 += 1
            

''' 
틀려서 구글 봄 너무 간단함 입력받은 수를 반갈 쳐서 
앞에는 빼면서 뒤에는 더하면서 입력값이랑 비교해보면 됨...
자괴감ㅂ라랒우랒랒루ㅏㄹ
8의 소수를 찾기
소수 리스트에 넣기
작은 수부터 하나씩 소수끼리 더하기
숫자가 8이면 더한 숫자 킵하기
킵할 때 조건으로 1번숫자가 2번보다 클 때
else로 2번 보다 작으면 break 걸기
1번 2번 출력하기
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
t 
예제 입력 1 
3
8
10
16
예제 출력 1 
3 5
5 5
5 11

'''