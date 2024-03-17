import sys
from collections import deque
input = sys.stdin.readline

def solve(n, graph):
    # dp [방향][행][열] 머리가 오는 수
    dp = [[[0 for i in range(n)] for j in range(n)] for k in range(3)]   
    dp[0][0][1] = 1
    for i in range(2, n):
        if graph[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]
    
    for r in range(1, n):
        for c in range(1, n):
            # 대각
            if graph[r][c] == 0 and graph[r][c-1] == 0 and graph[r-1][c] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

            #가로 세로
            if graph[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
    
    ans = sum(dp[i][n-1][n-1] for i in range(3))     
    return ans

def main():
    n = int(input())
    graph = [list(map(int,input().split())) for i in range(n)]
    
    print(solve(n, graph))

if __name__ == '__main__':
    main()