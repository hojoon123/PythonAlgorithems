import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
        
    if dp[x][y] != -1:
        return dp[x][y]
        
    ways = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n or graph[nx][ny] >= graph[x][y]:
            continue
        ways += dfs(nx, ny)
    
    dp[x][y] = ways
    return dp[x][y]

if __name__ == '__main__':
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    m, n = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(m)]
    dp = [[-1 for i in range(n)] for j in range(m)]
    print(dfs(0, 0))