import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, a, b, m, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                
    return

def main():
    t = int(input())
    
    for i in range(t):
        cnt = 0
        m, n, k = map(int,input().split())
        graph = [[0 for i in range(n)] for j in range(m)]

        for i in range(k):
            x, y = map(int,input().split())
            graph[x][y] = 1
        
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    cnt += 1
                    bfs(graph, i, j, m, n)
        print(cnt)
                    
        
        
if __name__ == "__main__":
    main()
    

'''
상하좌우 네 방향

첫 줄에는 테스트 케이스의 개수 T
M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50)
배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)


예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1 
5
1
'''