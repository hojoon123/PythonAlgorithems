import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
        
def bfs(graph, water):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        
        # 범람
        tmp = []
        while water:
            wx, wy = water.pop()
            
            for i in range(4):
                nwx = dx[i] + wx
                nwy = dy[i] + wy
                
                if nwx < 0 or nwx >= m or nwy < 0 or nwy >= n or graph[nwx][nwy] == '*':
                    continue
                
                if graph[nwx][nwy] == '.':
                    graph[nwx][nwy] = '*'
                    tmp.append((nwx,nwy))
                
        water = tmp
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or graph[nx][ny] == '*':
                continue
            
            q.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1
            if end == (nx,ny):
                return graph[nx][ny]
            
    return "KAKTUS"

if __name__ == '__main__':
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    m, n = map(int,input().split())
    graph = [list(map(str,input().rstrip())) for i in range(m)]
    water = []
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'S':
                start = (i,j)
                graph[i][j] = 0
            elif graph[i][j] == 'D':
                end = (i,j)
            elif graph[i][j] == '*':
                water.append((i,j))
                
    print(bfs(graph, water))