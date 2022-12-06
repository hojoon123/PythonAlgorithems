import sys
input = sys.stdin.readline
N, K = map(int,input().split())
dp = [[1 for i in range(K+1)] for j in range(N+1)]
for i in range(1,N+1):
    for j in range(2,K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N][K] % 1000000000)
'''
N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)
1000000000으로 나눈 나머지를 출력
예제 입력 1 
20 2,
예제 출력 1 
21
'''