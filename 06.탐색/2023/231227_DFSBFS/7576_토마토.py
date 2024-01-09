import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, m, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                

def main():
    cnt = 0
    m, n = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    bfs(graph, m, n)
    
    for i in graph:
        for j in i:
            if j == 0:
                print(-1)
                exit()
        cnt = max(cnt, max(i))
    #처음에 익은 토마토 개수 1로 해주었으니 최고값에서 1을 빼야 날짜가 나온다
    print(cnt - 1)
                    
        
        
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