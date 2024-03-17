from sys import stdin
input = stdin.readline

def dp(maxtrixs, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    
    for term in range(1, n):
        for start in range(n):
            if start + term == n:
                break
            dp[start][start+term] = int(1e9)
            
            for i in range(start, start+term):
                dp[start][start+term] = min(dp[start][start+term],
                                            dp[start][i] + dp[i+1][start+term] + maxtrixs[start][0] * maxtrixs[i][1] * maxtrixs[start+term][1])
    return dp[0][n - 1]

def main():
    n = int(input())
    maxtrixs = [list(map(int,input().split())) for i in range(n)]
    print(dp(maxtrixs, n))

if __name__ == "__main__":
    main()