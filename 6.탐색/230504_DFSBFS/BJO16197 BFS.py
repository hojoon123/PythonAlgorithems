from collections import deque
import sys

def bfs():
    queue = deque([(coin[0], coin[1], coin[2], coin[3], 0)])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    while queue:
        r1, c1, r2, c2, cnt = queue.popleft()
        if cnt >= 10:
            break

        for i in range(4):
            nr1, nc1 = r1+dr[i], c1+dc[i]
            nr2, nc2 = r2+dr[i], c2+dc[i]
            move = [1, 1]

            # 둘 다 나간 경우
            if not verify(nr1, nc1) and not verify(nr2, nc2):
                continue

            # 하나만 나간 경우
            if not verify(nr1, nc1) or not verify(nr2, nc2):
                return cnt + 1

            # 둘 다 안나간 경우
            if arr[nr1][nc1] == '#':
                nr1, nc1 = r1, c1
                move[0] = 0
            if arr[nr2][nc2] == '#':
                nr2, nc2 = r2, c2
                move[1] = 0
            if move[0] or move[1]:
                if not move[0] and not move[1]:
                    pass
                else:
                    queue.append((nr1, nc1, nr2, nc2, cnt+1))
    return -1


def verify(r, c):
    if r < 0 or r >= N or c < 0 or c >= M:
        return 0
    return 1

if __name__ == '__main__':
    N, M  = map(int,input().split())
    arr = [list(map(str,input().rstrip())) for i in range(N)]
    ans = 11
    coin = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'o':
                coin.append(i)
                coin.append(j)

    ans = bfs()
    print(ans)