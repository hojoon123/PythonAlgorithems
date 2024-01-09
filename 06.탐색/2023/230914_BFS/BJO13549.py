from sys import stdin
from collections import deque
input = stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    cnt[n] = 0
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(cnt[x])
            return
        
        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx <= max:
                if cnt[nx] == 0:
                    if nx == 2*x and nx != 0:
                        cnt[nx] = cnt[x]
                        q.appendleft(nx)
                    else:
                        cnt[nx] = cnt[x] + 1
                        q.append(nx)
                
                if cnt[nx] > cnt[x] + 1:
                    cnt[nx] = cnt[x] + 1
                elif cnt[nx] > cnt[x] and nx == 2*x:
                    cnt[nx] = cnt[x]

if __name__ == '__main__':
    n, k = map(int,input().split())
    max = 10 ** 5
    cnt = [0] * (max + 1)
    bfs(n)