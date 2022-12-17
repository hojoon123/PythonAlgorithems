import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int,input().split())
numbers = sorted(map(int, input().split()))
visited = [False] * N
arr = []
def dfs(start):
    if len(arr)==M:
        print(*arr)
        return
    overlap = 0
    for i in range(start,N):
        if not visited[i] and overlap != numbers[i]:
            visited[i] = True
            arr.append(numbers[i])
            overlap = numbers[i]
            dfs(i)
            visited[i] = False
            arr.pop()
        
dfs(0)
'''
예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5
'''