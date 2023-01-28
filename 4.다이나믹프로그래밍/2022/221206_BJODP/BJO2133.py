import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * 31
dp[0] = 1; dp[2] = 3; dp[4] = 11 
if N % 2 != 0:
    print(dp[N])
    exit()
for i in range(6,N+1,2):
    dp[i] = dp[i-2] * dp[2]
    for j in range(0, i-2, 2):
        dp[i] = dp[i] + dp[j] * 2
print(dp[N])

'''
예제 입력 1 
2
예제 출력 1 
3
'''