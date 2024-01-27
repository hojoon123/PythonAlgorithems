from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(n):
    arr = [(2 * i) - 1 for i in range(1,n + 1)]
    return arr
    
def main():
    n = int(input())
    print(*solve(n))
    
    
if __name__ == "__main__":
    main()
