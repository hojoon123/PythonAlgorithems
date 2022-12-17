import sys
from math import lcm
input = sys.stdin.readline
def cal(m,n,x,y):
    while x <= m * n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1
T = int(input())
for i in range(T):
    m,n,x,y = map(int,input().split())
    print(cal(m,n,x,y))

        

'''
(1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N)
예제 입력 1 
3
10 12 3 9
10 12 7 2
13 11 5 6
예제 출력 1 
33
-1
83
'''