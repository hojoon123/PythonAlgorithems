import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, a, b, N):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
                
    return cnt

def main():
    N = int(input())
    house = []
    graph = [list(map(int,input().rstrip())) for i in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                cnt = bfs(graph, i, j, N)
                house.append(cnt)
                
    house.sort()
    print(len(house))
    for i in house:
        print(i)
        
if __name__ == "__main__":
    main()