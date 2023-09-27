from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y):
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  return graph[N-1][M-1]

N, M = map(int, input().split())
graph = [list(map(int,input().rstrip())) for i in range(N)]
print(bfs(0, 0))


'''
예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
'''