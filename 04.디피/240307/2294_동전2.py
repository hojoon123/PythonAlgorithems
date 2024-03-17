from sys import stdin
input = stdin.readline

def check(coins, n, k):
    coins = list(set(coins))
    
    dp = [int(1e9) for i in range(k + 1)]
    dp[0] = 0
        
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[k] != int(1e9):
        return dp[k]
    else:
        return -1
    
def main():
    n, k = map(int,input().split())
    coins = [int(input()) for i in range(n)]
    print(check(coins, n, k))
    


if __name__ == "__main__":
    main()