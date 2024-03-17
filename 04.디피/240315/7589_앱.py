from sys import stdin
input = stdin.readline

def dp(n, k, graph, costs):
    sum_cost = sum(costs)
    dp = [[0 for i in range(sum_cost + 1)] for j in range(n + 1)]
    ans = int(1e9)
    for i in range(1, n+1):
        byte = graph[i]
        cost = costs[i]
        
        for j in range(sum_cost + 1):
            if j < cost: #현재 앱을 비활성화할만큼의 cost가 충분하지 않을 경우
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - cost] + byte)
            if dp[i][j] >= k:
                ans = min(ans, j)
    return ans

def main():
    n, k = map(int,input().split())
    graph = [0] + list(map(int,input().split()))
    cost = [0] + list(map(int,input().split()))
    print(dp(n, k, graph, cost))

if __name__ == "__main__":
    main()