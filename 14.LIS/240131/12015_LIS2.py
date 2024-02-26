import sys
import bisect
input = sys.stdin.readline

def solve(n, arr):
    dp = [arr[0]]
    for i in range(n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else: # dp가 정렬되어있을 경우 arr[i]의 인덱스 반환
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    return len(dp)
            
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n, arr))
        
if __name__ == "__main__":
    main()