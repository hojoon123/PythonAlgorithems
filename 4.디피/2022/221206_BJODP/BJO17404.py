import sys
input = sys.stdin.readline
N = int(input())
RGB = []
INF = 1001000
ans = INF
for i in range(N): RGB.append(list(map(int,input().split())))

for k in range(3):
    dp = [[INF for i in range(3)] for i in range(N)]
    dp[0][k] = RGB[0][k]
    for i in range(1,N):
        dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    for j in range(3):
        if k != j:
            ans = min(ans, dp[-1][j])
print(ans)
    
'''
1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 
예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
110
    if RGB[i-1][0] == fir_min:
        RGB[i][0] = min(RGB[i-1][1],RGB[i-1][2]) + RGB[i][0]
        RGB[i][1] = RGB[i-1][2] + RGB[i][1]
        RGB[i][2] = RGB[i-1][1] + RGB[i][2]
        
    elif RGB[i-1][1] == fir_min:
        RGB[i][0] = RGB[i-1][2] + RGB[i][0]
        RGB[i][1] = min(RGB[i-1][0],RGB[i-1][2]) + RGB[i][1]
        RGB[i][2] = RGB[i-1][0] + RGB[i][2]
'''