import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    print(3)
    exit()
dp =[0 for i in range(N+1)]
dp[1] = 3; dp[2] = 7
for i in range(3,N+1):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[N])

'''
1 ≤ N ≤ 100,000
9901로 나눈 나머지를 출력
예제 입력 1 
4
예제 출력 1 
41
'''