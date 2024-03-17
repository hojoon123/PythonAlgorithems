import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs():
    global visited
    q = deque()
    years = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] != 0:
                q.append((graph[i][j], i , j))
                
    tmp = deque()
    while True:
        while q:
            target, x, y = q.popleft()
            cnt = 0
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                if graph[nx][ny] == 0:
                    cnt += 1
            if target - cnt > 0:
                tmp.append((target-cnt, x, y))
            else:
                tmp.append((0, x, y))
        
        # 빙산 업데이트
        years += 1
        if tmp:
            q = copy.deepcopy(tmp)
            tmp.clear()
            for v ,dir_x, dir_y in q:
                graph[dir_x][dir_y] = v
        kk = 0
        for k,_,__ in q:
            if k != 0:
                kk = k
        if kk == 0:
            return 0
    
        # 분리 체크
        visited = [[0 for i in range(n)] for j in range(m)]
        check = False
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and graph[i][j] != 0:
                    visited[i][j] = 1
                    if check:
                        return years
                    check = True
                    dfs(i,j, check)


def dfs(x, y, check):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and graph[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny, check)
    
        

if __name__ == '__main__':
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    m, n = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(m)]
    print(bfs())