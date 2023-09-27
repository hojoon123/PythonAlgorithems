import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int,input().split())
numbers = sorted(map(int, input().split()))
visited = [False] * N
arr = []
def dfs():
    if len(arr)==M:
        print(*arr)
        return
    overlap = 0
    for i in range(N):
        if overlap != numbers[i]:
            arr.append(numbers[i])
            overlap = numbers[i]
            dfs()
            arr.pop()
        
dfs()
'''
예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5
'''