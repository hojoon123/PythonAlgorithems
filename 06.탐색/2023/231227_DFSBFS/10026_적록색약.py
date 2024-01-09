import sys
from collections import deque
import copy
input = sys.stdin.readline

def bfs(graph, n, cnt, dx, dy):
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != '0':
                q.append((i, j))
                cur_color = graph[i][j]
                graph[i][j] = '0'
                cnt += 1
                
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        
                        if graph[nx][ny] == cur_color:
                            graph[nx][ny] = '0'
                            q.append((nx, ny))
                            
    return cnt


def main():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = int(input())
    graph = [list(map(str,input().rstrip())) for i in range(n)]
    tmp_graph = copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "R":
                graph[i][j] = "G"
    
    ans = [0,0]
    ans[0] = bfs(tmp_graph, n, ans[0], dx, dy)
    ans[1] = bfs(graph, n, ans[1], dx, dy)
    
    print(*ans)
    
if __name__ == "__main__":
    main()