import sys
input = sys.stdin.readline
N = int(input())
dp = [i for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[N])
'''
제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력
예제 입력 1 
7
1
4
11
예제 출력 1 
4
1
1
3
'''