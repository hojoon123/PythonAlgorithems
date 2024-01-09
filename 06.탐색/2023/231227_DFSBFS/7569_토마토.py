import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, m, n, h):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dh = [1,-1]
    queue = deque()
    
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    queue.append((k, i, j))
                
    while queue:
        height, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[height][nx][ny] == 0:
                graph[height][nx][ny] = graph[height][x][y] + 1
                queue.append((height, nx, ny))
                
        for k in dh:
            nh = height + k
            if  0 <= nh < h and graph[nh][x][y] == 0:
                graph[nh][x][y] = graph[height][x][y] + 1
                queue.append((nh, x, y))
            
def main():
    cnt = 0
    m, n, h = map(int,input().split())
    graph = []
    for i in range(h):
        graph.append([list(map(int,input().split())) for i in range(n)])
    bfs(graph, m, n, h)
    
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit()
            cnt = max(cnt, max(j))
    #처음에 익은 토마토 개수 1로 해주었으니 최고값에서 1을 빼야 날짜가 나온다
    print(cnt - 1)
                    
        
        
if __name__ == "__main__":
    main()
    