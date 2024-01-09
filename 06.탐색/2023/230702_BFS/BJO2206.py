import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(a, b,c):
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = 1
    while q:
        x, y, wall = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                q.append((nx,ny,wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1
            
            if arr[nx][ny] == 1 and wall == 1:
                q.append((nx,ny,0))
                visited[nx][ny][0] = visited[x][y][wall] + 1
    return -1    
        
    
    


if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int,input().split())
    arr = [list(map(int,input().rstrip())) for i in range(n)]
    visited = [[[0] * 2 for i in range(m)] for j in range(n)]
    print(bfs(0,0,1))
    
'''
벽1 개 부수기 가능

N개의 줄에 M개의 숫자로 맵
N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
(1, 1)과 (N, M)은 항상 0
최단 거리를 출력한다. 불가능할 때는 -1을 출력
예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1
'''