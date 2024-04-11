import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(r, c, graph, dx, dy, start):
    visited = [[0 for i in range(c)] for j in range(r)]
    
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    cnt = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            
            if not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                if visited[nx][ny] > cnt:
                    cnt = visited[nx][ny]
    return cnt
                    
    
def main():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    r, c = map(int,input().split())
    graph = [list(map(str,input().rstrip())) for i in range(r)]
    ans = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'W':
                continue
            
            tmp = bfs(r,c,graph,dx,dy,(i, j))
            if tmp > ans:
                ans = tmp 
    if ans:
        print(ans-1)
    else:
        print(ans)
    
    
if __name__ == '__main__':
    main()