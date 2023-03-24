import sys
from collections import deque

input = sys.stdin.readline


def bfs(r,c,shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    tmp = []
    while q:
        cur_r,cur_c = q.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0<= nr < n and 0<= nc < n and visited[nr][nc] == 0:
                if ocean[nr][nc] <= shark_size:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[cur_r][cur_c] + 1
                    
                    if ocean[nr][nc] < shark_size and ocean[nr][nc] != 0:
                        tmp.append((nr,nc,distance[nr][nc]))

    return sorted(tmp,key=lambda x: (-x[2],-x[0],-x[1]))

if __name__ == '__main__':
    n = int(input())
    ocean = [list(map(int,input().split())) for i in range(n)]
    dr = [0,0,1,-1] # 0 우 1 왼 2 하 3 상
    dc = [1,-1,0,0]
    exp = 0
    size = 2
    answer = 0
    for i in range(n):
        for j in range(n):
            if ocean[i][j] == 9:
                r, c = i, j

    while 1:
        shark = bfs(r,c,size)

        if len(shark) == 0:
            break
        
        nr,nc,dist =shark.pop()
        answer += dist
        ocean[r][c],ocean[nr][nc] = 0,0
        r,c = nr,nc
        exp += 1
        if exp == size:
            size += 1
            exp = 0
    print(answer)
'''
예제 입력 4 
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
예제 출력 4 
60
'''