N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    dp[i] = p[i]
    for k in range(1,i+1):
        dp[i] = min(dp[i], dp[i-k] + p[k])
print(dp[i])

'''

최소값
예제 입력 1 
4
1 5 6 7
예제 출력 1 
4
'''