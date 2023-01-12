from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
arr = [int(input().rstrip()) for i in range(N)]
dp = [0 for i in range(K + 1)]
dp[0] = 1

for i in arr:
    for j in range(i, K + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[K])
#특정 코인을 썼을 때 각 자리별로 가지수 넣기 j - i개를 추가하면 해당 코인을 사용하였을 때
#이전의 가지수가 더해짐

'''
n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
예제 입력 1 
3 10
1
2
5
예제 출력 1 
10
'''