from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1
    idx = 1
    
    while queue:
        x = queue.popleft()
        children = []
        
        for i in link[x]:
            if visited[i] == 0:
                visited[i] = 1
                children.append(i)
                
        c_len = len(children)
        tmp = ans[idx : idx + c_len]
        if set(tmp) == set(children):
            queue.extend(tmp)
            idx += c_len
        else:
            return 0
    
    return 1
        
        
N = int(input())
link = [[] for i in range(N + 1)]
visited = [0] * (N + 1)

for i in range(N - 1):
    a, b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
    
ans = tuple(map(int,input().split()))


if ans[0] == 1:
    print(bfs())
else:
    print(0)

'''
정점의 수 N(2 ≤ N ≤ 100,000)
트리의 간선 정보
마지막 줄에는 BFS 방문 순서
1부터 N까지 자연수가 한 번씩 등장
올바른 순서는 1, 2, 3, 4와  1, 3, 2, 4가 있다.
BFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력
예제 입력 1 
4
1 2
1 3
2 4
1 2 3 4
예제 출력 1 
1

예제 입력 2 
4
1 2
1 3
2 4
1 2 4 3
예제 출력 2 
0
'''