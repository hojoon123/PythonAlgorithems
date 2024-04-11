import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    # dp[i][j]는 i번째 파일부터 j번째 파일을 합치는 최소값
    dp = [[0]*(n+1) for _ in range(n+1)]

    # 먼저 dp[i][i+1]을 구한다. 즉, 두 파일이 연속으로 되어있을 때의 합을 구하는 경우만 dp에 저장한다.
    for i in range(1, n):
        dp[i][i+1] = arr[i] + arr[i+1]

    # dp의 맨 밑에서부터 위로 올라오면서 dp를 채워 나간다.
    # dp[1][4]는 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4]와 같은 경우의 수를 가진다.
    for i in range(n-1, 0, -1):
        for j in range(1, n+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(arr[i:j+1])
    
    print(dp[1][n])

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        solve()