import sys
input = sys.stdin.readline
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = list(map(str,input().split()))
ans = 0
b = int(n[1])
s = list(n[0])
t = len(s) - 1
for i in range(t, -1, -1):
    ans += tmp.index(s[i]) * (b** (t-i))


print(ans)
'''
예제 입력 1 
ZZZZZ 36
예제 출력 1 
60466175
예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
'''