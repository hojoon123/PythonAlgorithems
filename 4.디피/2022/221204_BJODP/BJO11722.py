import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
result = []
dp = [1 for i in range(N)]
for i in range(1,N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))


'''
예제 입력 1 
6
10 30 10 20 20 10
예제 출력 1 
3
'''