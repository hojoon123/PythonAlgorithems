import sys
from collections import deque
import copy
input = sys.stdin.readline

#서순: 입력 받기 -> 백트래킹으로 벽 세우기 -> BFS로 바이러스 번식 -> 안전구역 탐색 및 갱신
def bfs():
    global answer
    cnt = 0
    q= deque()
    tmp_zido = copy.deepcopy(zido)
    for i in range(N):
        for j in range(M):
            if tmp_zido[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_zido[nx][ny] == 0:
                tmp_zido[nx][ny] = 2
                q.append((nx, ny))
    

    for i in range(N):
        cnt += tmp_zido[i].count(0)
    answer = max(answer, cnt)

def makeWall(cnt): # 백트래킹을 통해서 벽 세우기
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if zido[i][j] == 0:
                zido[i][j] = 1
                makeWall(cnt+1)
                zido[i][j] = 0
              
if __name__ == '__main__':
    N, M = map(int,input().split())
    zido = [list(map(int,input().split())) for i in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    makeWall(0)
    print(answer)