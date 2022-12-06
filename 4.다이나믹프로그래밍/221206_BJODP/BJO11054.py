import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
reverse_arr =arr[::-1]
result = [0 for i in range(N)]
dp = [1 for i in range(N)]
dp2 = [1 for i in range(N)]

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]: #증가
            dp[i] = max(dp[i], dp[j]+1)
        if reverse_arr[i] > reverse_arr[j]: #감소
            dp2[i] = max(dp2[i], dp2[j]+1)
for i in range(N): #서로 더하고 본인 중복 제거 
    result[i] = dp[i] + dp2[N-i-1] -1
print(max(result))

'''
예제 입력 1 
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1 
7
'''