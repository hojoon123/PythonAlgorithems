import sys
input = sys.stdin.readline


def bf():
    # 포인트 2 r,c 와 x,y 를 헷갈리지 말 것...
    n, m = map(int,input().split())
    r, c, d = map(int,input().split())
    room = [list(map(int,input().split())) for i in range(n)]
    visited = [[0] * m for i in range(n)]
    
    visited[r][c] = 1
    cnt = 1
    while 1:

        for i in range(4):
            d = (d + 3) % 4
            nx = dx[d] + r
            ny = dy[d] + c
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            

            if visited[nx][ny] == 0 and room[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                break
        else:
            if room[r - dx[d]][c - dy[d]] == 1:
                return cnt
            
            else:
                r, c = r -dx[d], c - dy[d]


if __name__ == '__main__':
    # 포인트 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    print(bf())
'''
1현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소

2현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우

2- 1바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번
2 -2바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

3현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
3 -1왼쪽 방향으로 90 회전
3 -2바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
3 -3 돌아간다.1번

0 북 1 동 2 남 3 서
예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1
예제 입력 2 
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57
'''