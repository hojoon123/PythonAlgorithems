import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 3
if n < 3: print(dp[n])
else:
    for i in range(3,n+1):
        dp[i] = (dp[i-1]%10007 + (dp[i-2] * 2)%10007)%10007
    print(dp[n])

'''

예제 입력 1 
2
8
예제 출력 1 
3
171
'''