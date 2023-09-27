import sys
input = sys.stdin.readline
N = int(input())
dp = [[1 for i in range(10)] for i in range(N+1)]
for i in range(10,1,-1): dp[1][-i] = i
for i in range(2,N+1):
    res = sum(dp[i-1])
    for j in range(10):
        if j == 0:
            dp[i][j] = res
        else:
            dp[i][j] = res - dp[i-1][j-1]
            res = dp[i][j]
print(sum(dp[N-1]) % 10007)

#for i in range(N+1):
    

'''
1 ≤ N ≤ 1,000
10007로 나눈 나머지를 출력
예제 입력 1 
1
2
3
예제 출력 1 
10
55
220
'''