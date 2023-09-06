from sys import stdin

input = stdin.readline


def dfs(cnt, r1, c1, r2, c2):
    global ans
    if cnt >= 10:
        return

    for i in range(4):
        nr1, nc1 = r1 + dr[i], c1 + dc[i]
        nr2, nc2 = r2 + dr[i], c2 + dc[i]
        move = [1, 1]

        if verify(nr1, nc1) == 0 and verify(nr2, nc2) == 0:
            continue

        if verify(nr1, nc1) and arr[nr1][nc1] == '#':
            nr1, nc1 = r1, c1
            move[0] = 0
        if verify(nr2, nc2) and arr[nr2][nc2] == '#':
            nr2, nc2 = r2, c2
            move[1] = 0

        if not move[0] and not move[1]:
            continue

        if verify(nr1, nc1) and verify(nr2, nc2):
            dfs(cnt + 1, nr1, nc1, nr2, nc2)
            continue

        ans = min(cnt + 1, ans)
def verify(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0
    return 1

if __name__ == '__main__':
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    n, m  = map(int,input().split())
    arr = [list(map(str,input().rstrip())) for i in range(n)]
    ans = 11
    coin = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'o':
                coin.append([i,j])

    dfs(0,coin[0][0],coin[0][1],coin[1][0],coin[1][1])

    if ans == 11:
        print(-1)
    else:
        print(ans)
'''
동시에 떨어지면 안됨
하나만 떨어뜨려야함.
벽 만나면 변동 사항 x
다 돌았을 때 ans = 0이면 -1 출력
if 하나만 떨구기 성공시 ans = 1 또 돌면서 ans 비교
ans 최고값으로 설정

5 3
###
.o.
###
.o.
###
예제 출력 4 
-1

예제 입력 5 
5 3
###
.o.
#.#
.o.
###
예제 출력 5 
3
'''