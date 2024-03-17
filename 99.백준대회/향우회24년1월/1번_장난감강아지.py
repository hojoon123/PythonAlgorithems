import sys
from collections import deque
input = sys.stdin.readline

def solve(s, n, k):
    curY = 0
    curX = 0

    if k > (n // 2):
        k = (n // 2)

    for _ in range(k):
        for c in s:
            if c == 'U':
                curY += 1
            elif c == 'D':
                curY -= 1
            elif c == 'L':
                curX -= 1
            else:
                curX += 1
            if curY == 0 and curX == 0:
                return "YES"

    return "NO"

def main():
    n, k = map(int,input().split())
    s = str(input().rstrip())
    
    print(solve(s, n, k))
    
if __name__ == "__main__":
    main()