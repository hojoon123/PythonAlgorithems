import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
        
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)
            
    return dp[x][y]
                
    
if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n = int(input())
    graph = [list(map(int,input().split())) for i in range(n)]
    dp = [[0 for i in range(n)] for j in range(n)]
    ans = 0
    
    for i in range(n):
        for j in range(n):
            if not dp[i][j]:
                dfs(i,j)
    
    for i in range(n):
        tmp = max(dp[i])
        if tmp > ans:
            ans = tmp
    print(ans)