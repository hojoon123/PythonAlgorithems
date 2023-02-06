import sys
from collections import deque
import copy
input = sys.stdin.readline
#빨라서 deque 씀
#원본은 놔둬야 해서 딥카피 때림
#서순 입력값 설정 > 백트래킹(벽 세우는 거 모든 가지수 탐색) > 바이러스 우다다다 돌리고 0 세기
def bfs(): #원본을 두고 벽을 생성한 지도를 deepcopy 때리고 2 돌리고 0 개수 탐색 후 비교
    global answer
    cnt = 0
    queue = deque()
    tmp_world = copy.deepcopy(world)
    for i in range(N):
        for j in range(M):
            if tmp_world[i][j] == 2:
                queue.append((i, j)) #모든 2의 좌표 따서 넣어둬 넣어둬
    
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 4딸라 방향으로 조져조져
            nx = x + dx[i] # 나는 누구 여긴 어디
            ny = y + dy[i] # 응애응애 공부하기 시러용 응애 살려주세요 진짜
            # 오늘 진짜 너무 많이 해서 어지러오욤 점심나가서먹을것같애
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_world[nx][ny] == 0:
                tmp_world[nx][ny] = 2
                queue.append((nx, ny))
    

    for i in range(N):
        cnt += tmp_world[i].count(0)
    answer = max(answer, cnt)
def makeWall(cnt): # 벽 백트래킹으로 모든 경우 탐색
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if world[i][j] == 0:
                world[i][j] = 1
                makeWall(cnt+1)
                world[i][j] = 0
                
N, M = map(int,input().split())
world = [list(map(int,input().split())) for i in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
makeWall(0)
print(answer)

'''
세로 크기 N 가로 크기 M (3 ≤ N, M ≤ 8)
0은 빈 칸, 1은 벽, 2는 바이러스
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
벽 3개 설치
벽 설치 백트래킹 쓰기
상 or 하 or 좌 or 우 == 0
    각각 2로 변경 
else:
    0의 개수 arr에 추가
    break

예제 입력 1 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1 
27
'''