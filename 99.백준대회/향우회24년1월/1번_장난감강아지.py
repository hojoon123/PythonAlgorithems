import sys
from collections import deque
input = sys.stdin.readline

def solve(s):

    tmp = [0,0]
    while s:
        t = s.pop()
        if t == "U":
            tmp[0] += 1
        elif t == "D":
            tmp[0] -= 1
        elif t == "R":
            tmp[1] += 1
        else:
            tmp[1] -= 1
            
        if tmp == [0,0]:
            return "YES"
    return "NO"

def main():
    n, k = map(int,input().split())
    s = list(map(str,input().rstrip()))
    
    print(solve(s))
    
if __name__ == "__main__":
    main()