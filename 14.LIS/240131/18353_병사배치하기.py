import sys
input = sys.stdin.readline

def solve(n, arr):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)
            
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    tmp = solve(n, arr[::-1])
    print(n - tmp)
    
if __name__ == "__main__":
    main()