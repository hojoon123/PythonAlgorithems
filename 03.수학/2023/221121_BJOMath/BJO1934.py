import sys
import math
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = list(map(int,input().split()))
    print(math.lcm(n[0],n[1]))


'''
예제 입력 1 
3
1 45000
6 10
13 17
예제 출력 1 
45000
30
221
'''