import sys
from collections import deque
input = sys.stdin.readline

def check(a, b):
    global cnt
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    world[a][b] = cnt
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and world[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                world[nx][ny] = cnt
                queue.append([nx, ny])


def distance(x):
    global ans
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if world[i][j] == x:
                queue.append([i, j])
                dist[i][j] = 0
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if world[nx][ny] > 0 and world[nx][ny] != x:
                answer = min(answer, dist[x][y])
                return

            if world[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append([nx, ny])


n = int(input())
world = [list(map(int,input().split())) for i in range(n)]
visited = [[False] * n for i in range(n)]
cnt = 1
ans = sys.maxsize
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    for j in range(n):
        if not visited[i][j] and world[i][j] == 1:
            check(i, j)
            cnt += 1


for i in range(1, cnt):
    distance(i)

print(ans)

'''
섬 찾기 섬 주위에 0들을 2로 바꾸고 카운트 증가 시키기
0이면 3으로 증가 시키기 반복 만약 1이 
예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
'''