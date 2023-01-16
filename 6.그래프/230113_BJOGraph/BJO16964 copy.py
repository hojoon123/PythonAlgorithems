import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(ans):
    tmp = ans.popleft()
    
    if not ans:
        print(1)
        exit(0)
        
    visited[tmp] = True
    
    for i in range(len(link[tmp])):
        if ans[0] in link[tmp] and visited[ans[0]] == False:
            dfs(ans) #이 생각을 했었는데 엉뚱하게 진행하였음.. 많이 공부 해야한다
    return False

n = int(input())
link = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
ans = deque(map(int,input().split()))

if ans[0] != 1:
    print(0)
    exit(0)
    
if not dfs(ans):
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
0
예제 입력 2 
4
1 2
1 3
2 4
1 2 4 3
예제 출력 2 
1
'''