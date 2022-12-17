import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int,input().split())
arr = []
def dfs():
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        arr.append(i)
        dfs()
        arr.pop()
dfs()
'''
예제 입력 2 
4 2
예제 출력 2 
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''