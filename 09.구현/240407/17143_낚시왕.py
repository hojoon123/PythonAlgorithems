import sys
from collections import deque
input = sys.stdin.readline

def move():
    global graph
    tmp_graph = [[[] for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                x, y = i, j
                z,s,d = graph[i][j][0]
                s_cnt = s
                
                while s_cnt > 0:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        # 방향전환
                        if d % 2: # 아래 왼
                            d -= 1
                        else: # 위 오른
                            d += 1
                        continue
                    else:
                        x, y = nx, ny
                        s_cnt -= 1
                tmp_graph[x][y].append([z,s,d])
    
    for i in range(n):
        for j in range(m):
            graph[i][j] = tmp_graph[i][j]
                    
def solve():
    ans = 0
    # 오른쪽 이동
    for i in range(m):
        for j in range(n):
            if len(graph[j][i]) > 0:
                value = graph[j][i][0] # 상어 크기추가
                ans += value[0]
                graph[j][i].remove(value)
                break
        
        move()

        for r in range(n):
            for c in range(m):
                if len(graph[r][c]) > 1:
                    graph[r][c].sort(reverse = True)
                    while len(graph[r][c]) > 1:
                        graph[r][c].pop()
    return ans

if __name__ == "__main__":
    dx = [-1,1,0,0] # 상하우좌
    dy = [0,0,1,-1]
    n, m, lc = map(int,input().split())
    graph = [[[] for i in range(m)] for j in range(n)]
    for i in range(lc):
        r,c,s,d,z = map(int,input().split())
        graph[r-1][c-1].append([z,s,d-1])
        
    print(solve())