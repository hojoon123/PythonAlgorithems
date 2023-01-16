import sys
from math import sqrt
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
    
'''
(4 ≤ N, M ≤ 500)

예제 입력 1 
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1 
19
'''