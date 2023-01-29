import sys
from math import sqrt
input = sys.stdin.readline
M , N = [int(input()) for i in range(2)]
res = 0; cnt = 0; res_min = 0
for i in range(M,N+1):
    if int(sqrt(i)) == sqrt(i): 
        res += i
        if cnt == 0:
            cnt += 1
            res_min = i
if res == 0: print(-1)
else: print(res); print(res_min)
'''
예제 입력 1 
60
100
예제 출력 1 
245
64
'''