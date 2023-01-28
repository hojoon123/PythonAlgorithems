import sys
input = sys.stdin.readline
N = int(input())
dp = [[0 for i in range(2)] for j in range(91)]
dp[1][0] = 1; dp[2][0] = 1
for i in range(3,N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[N]))
'''
dp[i][0] = dp[i-1][0] + dp[i-1][1]
dp[i][1] = dp[i-1][0]
sum(dp[N])
0으로 시작 x 
11 연속 x
N(1 ≤ N ≤ 90)
N은 자리수
예제 입력 1 
3
예제 출력 1 
2
'''