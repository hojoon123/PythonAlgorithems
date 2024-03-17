from sys import stdin
input = stdin.readline

def lcs(a, b):
    n, k = len(a), len(b)
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][k]
    

def main():
    word1 = input().rstrip()
    word2 = input().rstrip()
    print(lcs(word1,word2))


if __name__ == "__main__":
    main()