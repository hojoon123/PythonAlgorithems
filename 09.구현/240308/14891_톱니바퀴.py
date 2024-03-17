import sys
from collections import deque
input = sys.stdin.readline


def left(target, dir):
    if target < 0:
        return
    else:
        if cws[target][2] != cws[target + 1][6]:
            left(target - 1, -dir)
            cws[target].rotate(dir)

def right(target, dir):
    if target > 3:
        return
    else:
        if cws[target][6] != cws[target - 1][2]:
            right(target + 1, -dir)
            cws[target].rotate(dir)

if __name__ == '__main__':
    cws = [deque(map(int,input().rstrip())) for i in range(4)]
    k = int(input())
    patterns = [list(map(int,input().split())) for i in range(k)]
    ans = 0
    
    for pattern in patterns:
        target = pattern[0] - 1
        dir = pattern[1]
        left(target - 1, -dir)
        right(target + 1, -dir)
        cws[target].rotate(dir)
        
    for i in range(4):
        ans += cws[i][0] * (2**i)
    print(ans)
