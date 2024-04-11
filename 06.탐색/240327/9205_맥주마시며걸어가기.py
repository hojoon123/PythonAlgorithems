import sys
from collections import deque
input = sys.stdin.readline

def bfs(hx, hy):
    q = deque()
    q.append((hx,hy))
    
    while q:
        x, y = q.popleft()
        
        if abs(ex - x) + abs(ey - y) <= 1000:
            return 'happy'
        for i in range(len(graph)):
            if visited[i] == 1:
                continue
            if abs(graph[i][0] - x) + abs(graph[i][1] - y) <= 1000:
                q.append((graph[i]))
                visited[i] = 1
    return "sad"
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        hx, hy = map(int,input().split())
        graph = []
        for i in range(n):
            graph.append(tuple(map(int,input().split())))
        ex, ey = map(int,input().split())
        visited = [0] * (n+1)
        print(bfs(hx, hy))