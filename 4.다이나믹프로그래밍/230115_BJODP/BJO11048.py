from sys import stdin
input = stdin.readline

n, k = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]
dp = [[0] * (k + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = graph[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[n][k])
'''
현재 위치 = max(이전 위치 + 오른, 이전 위치 + 아래, 이전 위치 + 대각아래) 
 N, M이 주어진다. (1 ≤ N, M ≤ 1,000)
 크기
 오른 아래 대각 최대 갯수
예제 입력 1 
3 4
1 2 3 4
0 0 0 5
9 8 7 6
예제 출력 1 
31
'''