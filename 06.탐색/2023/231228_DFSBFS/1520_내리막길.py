import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, h, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:
                q.append((i, j))
                graph[i][j] = h
                cnt += 1
                
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h:
                            q.append((nx, ny))
                            graph[nx][ny] = h
    return cnt

            
def main():
    n = int(input())
    max_h = 0
    graph = []
    ans = 0
    for i in range(n):
        tmp = list(map(int,input().split()))
        graph.append(tmp)
        tmp_max = max(tmp)
        if max_h < tmp_max:
            max_h = tmp_max
    
    for h in range(max_h-1, -1, -1):
        cnt = bfs(graph, h, n)
        if cnt > ans:
            ans = cnt
            
    print(ans)
        
        
if __name__ == "__main__":
    main()
    