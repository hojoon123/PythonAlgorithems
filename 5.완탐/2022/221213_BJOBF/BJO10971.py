import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
cost = [list(map(int,input().split())) for i in range(N)]
min_value = sys.maxsize
def backtracking(start, next, value, visited):
    global min_value
    
    if len(visited) == N: 
        if cost[next][start] != 0: 
            min_value = min(min_value, value + cost[next][start]) 
        return
    
    for i in range(N):

        if cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i)
            backtracking(start, i, value + cost[next][i], visited)
            visited.pop()
            
#도시마다(0~3) 출발점을 지정
for i in range(N):
    backtracking(i, i, 0, [i])

print(min_value)
'''
 (2 ≤ N ≤ 10)
 N개의 줄에는 비용 행렬
  1,000,000 이하의 양의 정수 갈 수 없는 경우는 0
  W[i][j]
예제 입력 1 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
예제 출력 1 
35
'''