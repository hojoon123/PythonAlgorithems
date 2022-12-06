import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [1 for i in range(N)]
result = []
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_dp = max(dp)
print(max_dp)

max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()
print(*lis)
'''

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
10 20 30 50
'''