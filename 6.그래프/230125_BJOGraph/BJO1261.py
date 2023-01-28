from sys import stdin
from collections import deque
input = stdin.readline

def check(a, b):
    q = deque()
    q.append([a, b])
    dist[a][b] = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    if world[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        q.appendleft((nx, ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
    print(dist[m - 1][n - 1])
        

if __name__ == '__main__':
    n, m = map(int,input().split())
    world = [list(map(int,input().rstrip())) for i in range(m)]
    dist = [[-1] * n for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    check(0, 0)
    
'''
메모리 시간 조건이 좀 빡셈 이러면 그래프 하나에서 처리해야 함
충분하네 128이여도 서브 공간 만들 정도는 되는구나
(x+1, y), (x, y+1), (x-1, y), (x, y-1)
상하좌우 탐색
자리 마다 
미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)
0은 빈 방을 의미하고, 1은 벽
(1, 1)과 (N, M)은 항상 뚫려있다
알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력


0, 0 부터 시작해서 상하좌우 탐색
각 자리 마다 카운트로 체크 1이면 cnt + 1
0이면 cnt
0이면 cnt 도착점에 도달했을 때 왼쪽 오른쪽 중 cnt가 가장 적은 곳을 출력
if 다음 위치 == 1 
    다음위치 = 현재위치 + 1
    if arr[다음 위치] != 1 or arr[다음 위치] != 0
        다음 위치 = min(현재 위치, 다음 위치)
elif 다음 위치 == 0 
    다음위치 = 현재위치
else:
    다음 위치 = min(현재 위치, 다음 위치)

예제 입력 1 
3 3
011
111
110
예제 출력 1 
3
예제 입력 2 
4 2
0001
1000
예제 출력 2 
0
'''