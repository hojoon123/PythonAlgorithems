from sys import stdin
input = stdin.readline

def dp(maxtrixs, n):
    dp = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == int(1e9):
                dp[i][j] = maxtrixs[i][0] * maxtrixs[j][0] * maxtrixs[j][1]
            else:
                min(dp[i][j], maxtrixs[i][0] * maxtrixs[j][0] * maxtrixs[j][1])
    return dp

def main():
    n = int(input())
    maxtrixs = [list(map(int,input().split())) for i in range(n)]
    print(dp(maxtrixs, n))

if __name__ == "__main__":
    main()