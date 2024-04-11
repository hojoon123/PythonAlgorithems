import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(n, k):
    lines = [0] * 100001
    q = deque()
    q.append(n)
    cnt, ans = 0, 0
    
    while q:
        x = q.popleft()
        tmp = lines[x]
        if x == k:
            ans = tmp
            cnt += 1
            continue
        
        for nx in (x-1, x+1, 2*x):
            if nx < 0 or nx >= 100001:
                continue
            
            if lines[nx] == 0 or lines[nx] == lines[x] + 1:
                lines[nx] = lines[x] + 1
                q.append(nx)
                
    return cnt, ans
    
if __name__ == '__main__':
    n, k = map(int,input().split())
    cnt, ans = bfs(n,k)
    print(ans)
    print(cnt)