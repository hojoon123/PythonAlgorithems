import sys
from collections import deque
input = sys.stdin.readline

# 치즈 녹이기
# while True 돌리면서 최초에 1이 있는지 체크 
# 0 0 시작 bfs 돌리기
# 

def bfs(graph):
    visited = [[0 for i in range(c)] for j in range(r)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 1:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                visited[nx][ny] = 1
            else:
                q.append((nx,ny))
                visited[nx][ny] = 1
    
if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    r, c =map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(r)]
    cnt, last_cheeze = 0, 0

    while True:
        cheezes = 0
        for i in range(r):
            cheezes += graph[i].count(1)
        
        if cheezes == 0:
            print(cnt)
            print(last_cheeze)
            break
        
        last_cheeze = cheezes
        cnt += 1
        bfs(graph)