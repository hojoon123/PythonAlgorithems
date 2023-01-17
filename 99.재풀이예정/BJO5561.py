from sys import stdin

input = stdin.readline

n = int(input())
dp1 = [0] * n
dp2 = [0] * n
for i in range(1, n):
    x = int(input())
    
    for j in range(i, 1, -1):
        dp2[j] = min(dp1[j - 1], dp1[i + 1 - j] + x)
        dp2[1] = x
        copy(dp2, dp2 + 1 + i, dp1)
print(dp1[n / 2])

'''
dp[n][m]: 1...n 과자 중 n을 포함해 m개 가지기 위해 필요한 최소 힘
dp[n][m]=min(dp[n-1][m-1],dp[n-1][n-m]+a[n-1])

예제 입력 1 
6
1
8
12
6
2
예제 출력 1 
7
'''