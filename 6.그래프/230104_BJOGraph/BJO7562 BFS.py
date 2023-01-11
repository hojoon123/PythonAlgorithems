import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    if a == X2 and b == Y2:
        return 0
    
    queue = deque()
    queue.append([a, b])
    world[a][b] = 1 #안 해도 차이 없을 듯 근데 확장성을 고려해서 미리 해두고 1 빼기로 감
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and world[nx][ny] == 0:
                world[nx][ny] = world[x][y] + 1
                
                if nx == X2 and ny == Y2:
                    return world[nx][ny] - 1
                
                queue.append([nx, ny])

T = int(input())
dx = [-2, -1, -2, -1, 1, 2, 1 ,2]
dy = [-1, -2, 1, 2, 2, 1, -2, -1]

for i in range(T):
    N = int(input()) #변의 길이
    X1, Y1 = map(int,input().split()) # 시작 칸
    X2, Y2 = map(int,input().split()) # 목표 칸
    world = [[0] * N for i in range(N)]
    print(bfs(X1, Y1))

'''
dx = []
dy = []
나이트가 최소 몇 번만에 이동할 수 있는지 출력
예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
'''