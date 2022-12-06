import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
result = []
dp = arr[:]
for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + arr[i])
print(max(dp))


'''
1 ≤ N ≤ 1,000
1 ≤ arr[i] ≤ 1,000
예제 입력 1 
10
1 100 2 50 60 3 5 6 7 8
예제 출력 1 
113
예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
10 20 30 50
'''