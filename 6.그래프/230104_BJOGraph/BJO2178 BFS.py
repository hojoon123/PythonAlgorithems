import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

bfs(M,N)

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(i))
#처음에 익은 토마토 개수 1로 해주었으니 최고값에서 1을 빼야 날짜가 나온다
print(cnt - 1)

'''
영향은 상하좌우 cnt로 날짜 카운트
상자의 크기를 나타내는 두 정수 M,N 가로 세로
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

토마토가 모두 익을 때까지의 최소 날짜를 출력
저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
토마토가 모두 익지는 못하는 상황이면 -1을 출력

예제 입력 1 
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
예제 출력 1 
8
'''