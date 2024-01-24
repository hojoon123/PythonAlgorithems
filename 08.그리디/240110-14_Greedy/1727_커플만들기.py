import sys
input = sys.stdin.readline

def solve(man, woman, dp, n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i-1][j-1]+abs(man[i-1] - woman[j-1])
            if i > j:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            elif j > i:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
                
    return dp[n][m]

def main():
    n, m = map(int,input().split())
    man = sorted(map(int,input().split()))
    woman = sorted(map(int,input().split()))
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    print(solve(man, woman, dp, n, m))
    
if __name__ == "__main__":
    main()
