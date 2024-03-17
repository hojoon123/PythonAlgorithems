import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def fill(graph, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1
                
def dfs(depth, graph):
    global ans
    if depth == len(cctvs):
        cnt = 0
        for i in range(n):
            cnt += graph[i].count(0)
        if ans > cnt:
            ans = cnt
        return
    
    tmp_graph = copy.deepcopy(graph)
    cctv, x, y = cctvs[depth]
    for i in mode[cctv]:
        fill(tmp_graph, i, x, y)
        dfs(depth+1, tmp_graph)
        tmp_graph = copy.deepcopy(graph)
        
if __name__ == '__main__':
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],                    
    [[0, 1], [1, 2], [2, 3], [3, 0]],    
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
    ]

    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    cctvs =  []
    ans = int(1e9)
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and graph[i][j] != 6:
                cctvs.append((graph[i][j],i,j))
    dfs(0, graph)
    print(ans)
    
