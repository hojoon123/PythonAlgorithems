from sys import stdin
input = stdin.readline

def check(graph, n):
    dp = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if graph[i][1] > graph[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)
    
def main():
    n = int(input())
    graph = sorted([list(map(int,input().split())) for i in range(n)])
    print(check(graph, n))


if __name__ == "__main__":
    main()