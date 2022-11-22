import sys
input = sys.stdin.readline
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int,input().split())
ans = ''
while n != 0:
    ans += str(tmp[n % b])
    n = n // b
print(ans[::-1])
'''
2<= b <= 36
11 10 11 12
123456789A A1A2
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

첫째 줄에 10진법 수 N을 B진법으로 출력
예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
'''