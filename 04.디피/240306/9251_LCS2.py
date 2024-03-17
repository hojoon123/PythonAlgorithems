from sys import stdin
input = stdin.readline

def get_lcs(a, b, n, k):
    n, k = len(a), len(b)
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp
    

def main():
    word1 = input().rstrip()
    word2 = input().rstrip()
    n = len(word1)
    k = len(word2)
    dp = get_lcs(word1, word2, n, k)
    last_idx = dp[n][k]
    lcs = []
    
    for i in range(n, 0, -1):
        for j in range(k, 0, -1):
            if dp[i][j] == last_idx:
                if word1[i - 1] == word2[j - 1]:
                    lcs.append(word1[i - 1])
                    last_idx -= 1
                    break

    print(dp[n][k])
    print(*lcs[::-1], sep="")

if __name__ == "__main__":
    main()