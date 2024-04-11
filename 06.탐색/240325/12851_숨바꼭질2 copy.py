import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(n, k):
    q = deque()
    q.append((n,0))
    cnt = int(1e9)
    ans = 0
    
    while q:
        x, depth = q.popleft()
        
        for nx in (x-1, x+1, 2*x):
            if nx < 0 or nx >= 100001 or depth > cnt:
                continue
            if nx == k:
                cnt = depth
                ans += 1
                continue
            
            q.append((nx, depth+1))
    return cnt, ans
    
if __name__ == '__main__':
    n, k = map(int,input().split())
    cnt, ans = bfs(n,k)
    print(cnt+1)
    print(ans)