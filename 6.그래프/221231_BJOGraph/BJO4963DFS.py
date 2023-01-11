import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global land
    world[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and world[nx][ny] == 1:
            dfs(nx, ny)
    return

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

while 1:
    N, M = map(int,input().split())
    world = [[0] * N for i in range(M)]
    land = 0
    if N == 0 and M == 0:
        break
        
    for i in range(M):
        world[i] = list(map(int,input().split()))
    
    for i in range(M):
        for j in range(N):
            if world[i][j] == 1:
                dfs(i,j)
                land += 1
    print(land)
            


'''
무한 루프
첫째 줄에는 지도의 너비 w와 높이 h
w와 h는 50보다 작거나 같은 양의 정수
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다
섬의 개수를 출력

입력의 마지막 줄에는 0 0
예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
'''