import sys
from collections import deque
input = sys.stdin.readline

def solve(n, m, graph):
    dp = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = graph[i][j]
            elif graph[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    ans = 0
    for i in range(n):
        if max(dp[i]) > ans:
            ans = max(dp[i])
    return ans * ans

def main():
    n, m = map(int,input().split())
    graph = [list(map(int,input().rstrip())) for i in range(n)]
    print(solve(n, m, graph))
    

if __name__ == '__main__':
    main()