import sys
from collections import deque
input = sys.stdin.readline

def dp(n, graph, k):
    dp = [[0 for i in range(n)] for j in range(n)]
    # 1
    for i in range(n):
        dp[i][i] = 1
    # 2
    for i in range(n-1):
        if graph[i] == graph[i+1]:
            dp[i][i+1] = 1
    # 3
    for lens in range(2, n):
        for i in range(n - lens):
            j = i + lens
            if graph[i] == graph[j] and dp[i+1][j-1]:
                dp[i][j] = 1
        
    for i in range(k):
        a, b = map(int,input().split())
        print(dp[a-1][b-1])
        

def main():
    n = int(input())
    graph = list(map(int,input().split()))
    k = int(input())
    dp(n, graph, k)

if __name__ == '__main__':
    main()