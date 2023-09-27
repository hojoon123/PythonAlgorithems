import sys
input = sys.stdin.readline

def dfs(r, c, dsum, cnt):
    global answer
    
    if cnt == 4:
        if answer < dsum:
            answer = dsum
        return
    
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        
        if not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, dsum + board[nr][nc], cnt + 1)
            visited[nr][nc] = 0
        
def fuck(r, c):
    global answer
    for i in range(4):
        tmp = board[r][c]
        for k in range(3):
            d = (i + k) % 4
            nr = dr[d] + r
            nc = dc[d] + c
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                break
            
            tmp += board[nr][nc]
        if answer < tmp:
            answer = tmp
            

if __name__ == '__main__':
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    answer = 0
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(n)]
    visited = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            dfs(i, j, board[i][j] ,1)
            visited[i][j] = 0
            fuck(i, j)
            
    print(answer)
'''

세로 크기 N과 가로 크기 M
테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력
예제 입력 1 
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1 
19
'''