import sys

input = sys.stdin.readline

def dfs(r, c, cnt, dsum):
    global ans

    if ans >= dsum + mx_point * (4 - cnt):
        return
    if cnt==4:
        if ans < dsum:
            ans = dsum
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        
        if not visited[nr][nc]:
            if cnt == 2:
                visited[nr][nc] = True
                dfs(r, c, cnt + 1, dsum + board[nr][nc])
                visited[nr][nc] = False
            visited[nr][nc] = True
            dfs(nr, nc, cnt+1, dsum + board[nr][nc])
            visited[nr][nc] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    visited = [[False] * m for _ in range(n)]
    mx_point = max(map(max, board))
    ans = 0
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False
    print(ans)