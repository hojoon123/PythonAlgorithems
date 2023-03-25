from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1
    
    while queue:
        x = queue.popleft()
        
        for i in link[x]:
            if visited[i] == 0:
                visited[i] = 1
                children[x].add(i)
                queue.append(i)
        
        
N = int(input())
link = [[] for i in range(N + 1)]
visited = [0] * (N + 1)
children = [set() for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
    
ans = list(map(int,input().split()))
idx = 1

bfs()

for i in ans:
    if idx == N:
        break
    c_len = len(children[i])
    tmp = set(ans[idx : idx + c_len])
    if tmp != children[i]:
        print(0)
        exit()
    idx += c_len

print(1)