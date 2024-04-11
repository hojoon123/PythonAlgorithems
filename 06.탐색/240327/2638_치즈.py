import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(x, y):
    visited = [[0 for i in range(m)] for j in range(n)]
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 2:
                continue
            
            if visited[nx][ny] == 1:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = 2
                    graph[nx][ny] = 0
                else:
                    continue
                
            elif not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
            
    
if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    cnt = 0
    while True:
        for i in range(n):
            if graph[i].count(1):
                break
        else:
            break
        bfs(0,0)
        cnt += 1
    
    print(cnt)