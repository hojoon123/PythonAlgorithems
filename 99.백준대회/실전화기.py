from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(n, k):
    if k == n - 1 or k == 1:
        return 0
    if n == 4 and k == 2:
        return 1
    return int((n - 3) // 2 * n)
    
def main():
    n, k = map(int,input().split())
    print(solve(n,k))
    
if __name__ == "__main__":
    main()
