import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, z):
    visited = [[[0] * (k+1) for i in range(n)] for j in range(m)]
    q = deque()
    q.append((x,y,z))
    visited[x][y][z] = 1

    while q:
        x, y, z = q.popleft()
        
        if x == (m-1) and y == (n-1):
            return visited[x][y][z] - 1
                            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if not graph[nx][ny] and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))
        
        if z < k:
            for d in dn:
                nx = d[0] + x
                ny = d[1] + y
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                if not graph[nx][ny] and not visited[nx][ny][z+1]:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append((nx,ny,z+1))
                
    return -1
            
if __name__ == '__main__':
    k = int(input())
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(m)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dn = [[-2,-1], [-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

    print(bfs(0,0,0))