from sys import stdin
input = stdin.readline

def dp(graph, n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    # 현재 물건이 들어간 배낭의 가치 vs 이전 물건을 넣었을 때의 배낭의 가치
    for i in range(1, n+1):
        for j in range(1, k+1):
            w = graph[i][0]
            v = graph[i][1]
            
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
    return dp[n][k]
    

def main():
    n, k = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    graph.insert(0,[0,0])
    print(dp(graph, n, k))


if __name__ == "__main__":
    main()

'''
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

N개의 물건이 있다. 
각 물건은 무게 W와 가치 V
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
배낭에 넣을 수 있는 물건들의 가치의 최댓값

입력
물건의 수 n, 가방 무게 k
물건 무게 w, 가치 v

'''