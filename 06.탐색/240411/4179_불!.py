import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((pos_j[0][0], pos_j[0][1], "J"))  # 지훈이가 먼저 이동
    graph[pos_j[0][0]][pos_j[0][1]] = 0
    
    if len(pos_f) != 0:
        for (r, c) in pos_f:
            q.append((r, c, "F"))
            graph[r][c] = "#"

    while q:
        x, y, z = q.popleft()
        if z == "J" and (x == 0 or y == 0 or x == n - 1 or y == m - 1):  # 탈출가능
            if graph[x][y] == "#":
                continue
            
            return graph[x][y] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] != "#" and z == "F":
                graph[nx][ny] = "#"
                q.append((nx, ny, "F"))
                
            elif graph[nx][ny] == "." and z == "J" and graph[x][y] != "#":
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, "J"))
                
    return "IMPOSSIBLE"

if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    n, m = map(int,input().split())
    graph = []
    pos_j = []
    pos_f = []
    
    for i in range(n):
        tmp = list(input().rstrip())
        for j in range(m):
            if tmp[j] == "J":
                pos_j.append((i, j))
            elif tmp[j] == "F":
                pos_f.append((i, j))
        graph.append(tmp)

    print(bfs())
    