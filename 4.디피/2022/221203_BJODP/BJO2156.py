import sys
input = sys.stdin.readline
N = int(input())
arr = [0]
[arr.append(int(input())) for i in range(N)]
dp = [0]
dp.append(arr[1])
if N > 1:
    dp.append(arr[1]+arr[2])
for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1]))
print(dp[N])
'''
예제 입력 1 
6
6
10
13
9
8
1
예제 출력 1 
33
'''