import sys
input = sys.stdin.readline
N = int(input())
arr = []
[arr.append(list(map(int,input().split()))) for i in range(N)]
dp = [arr[0][0]]
tmp = []
for k in range(1,N):
    dp.append(dp[-1] + arr[k][-1])
    [tmp.append(max(dp[j-1], dp[j])+arr[k][j]) for j in range(1,k)]
    
    for j in range(1,k): 
        dp[j] = tmp.pop(0)
    dp[0] = dp[0] + arr[k][0]
print(max(dp))
'''
예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
'''