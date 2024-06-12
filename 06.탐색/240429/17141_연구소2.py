import sys
from collections import deque
import copy
input = sys.stdin.readline

def bfs(graph, start_virous):
    global ans
    cnt = 0
    q = deque()
    for v in start_virous:
        q.append(v)
        graph[v[0]][v[1]] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == -1:
                continue
            
            if graph[nx][ny] == -2:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    for i in range(n):
        tmp = max(graph[i])
        if min(graph[i]) == -2:
            return
        
        if tmp > cnt:
            cnt = tmp

    if ans > cnt:
        ans = cnt
        return
            
def backtracking(idx, cur_virous):
    if len(cur_virous) == m:
        tmp_graph = copy.deepcopy(graph)
        bfs(tmp_graph, cur_virous)
        return
    
    for i in range(idx, len_v):
        cur_virous.append(virous[i])
        backtracking(i + 1, cur_virous)
        cur_virous.pop()
    
if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int,input().split())
    graph = []
    virous = []
    ans = int(1e9)
    for i in range(n):
        a = list(map(int,input().split()))
        for j in range(len(a)):
            if a[j] == 2:
                virous.append((i,j))
                a[j] = -2
            elif a[j] == 1:
                a[j] = -1
            else:
                a[j] = -2
        graph.append(a)
    
    len_v = len(virous)
    backtracking(0, [])
    print(-1 if ans == int(1e9) else ans)
    