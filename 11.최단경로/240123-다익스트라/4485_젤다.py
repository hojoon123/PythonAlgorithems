import sys
import heapq
input = sys.stdin.readline

def solve(n, graph):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    distance = [[int(1e9)] * (n + 1) for i in range(n + 1)]
    distance[0][0] = 0 
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if x == n - 1 and y == n - 1:
            return distance[x][y]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] > dist + graph[nx][ny]:
                    distance[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    return
        

def main():
    cnt = 0
    while 1:
        cnt += 1
        n = int(input())
        if n == 0:
            return
        graph = [list(map(int,input().split())) for i in range(n)]
        print(f"Problem {cnt}: {solve(n, graph)}")
    
if __name__ == "__main__":
    main()