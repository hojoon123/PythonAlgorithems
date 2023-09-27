import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(101)]
for k in range(1,10): dp[1][k] = 1
for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N]) % 1000000000)
'''
1<= N <= 100
1000000000으로 나눈 나머지를 출력
예제 입력 1 
1
2
예제 출력 1 
9
17
'''