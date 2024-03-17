import sys
from collections import deque
input = sys.stdin.readline

# 확산
def spread(dust, dx, dy, r, c, graph):
    while dust:
        v,x,y = dust.pop()
        cnt = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
                continue
            
            graph[nx][ny] += v//5
            cnt += 1

        graph[x][y] -= (v // 5) * cnt
        
    return graph

def clean(up, down, dx, dy, r, c, graph):
    # 위에 회전
    x, y = up, 1
    idx = 1 # 오른쪽부터 시작
    tmp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx == r or ny == c or nx == -1 or ny == -1: # 벽에 닿았을 때
            idx = (idx - 1) % 4 # 우 상 좌 하
            continue
        if x == up and y == 0: # 공기청정기로 다시 돌아옴
            break
        graph[x][y], tmp = tmp, graph[x][y] # swap
        x,y = nx, ny
        
    # 아래 회전
    x, y = down, 1
    idx = 1 # 우부터 시작
    tmp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx == r or ny == c or nx == -1 or ny == -1: # 벽에 닿았을 때
            idx = (idx + 1) % 4 # 우 하 좌 상
            continue
        if x == down and y == 0: # 공기청정기로 다시 돌아옴
            break
        graph[x][y], tmp = tmp, graph[x][y] # swap
        x,y = nx, ny
    return graph

def main():
    r, c, t = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(r)]
    robot = []
    dust = []
    dx = [-1,0,1,0] # 상 우 하 좌
    dy = [0,1,0,-1]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                robot.append((i,j))
            elif graph[i][j] != 0:
                dust.append((graph[i][j],i,j))
                
    for t in range(t):
        graph = spread(dust, dx, dy, r, c, graph) # 확산
        graph = clean(robot[0][0],robot[1][0], dx, dy, r, c, graph) # 공기청정기
        
        # dust 다시 채우기
        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    dust.append((graph[i][j],i,j))
                    
    print(sum(dust[i][0] for i in range(len(dust))))

if __name__ == '__main__':
    main()