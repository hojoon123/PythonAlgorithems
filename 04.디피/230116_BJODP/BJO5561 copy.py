from sys import stdin

input = stdin.readline

n = int(input())
arr = [int(input()) for i in range(n - 1)]
dp = [0] * n


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