from sys import stdin
input = stdin.readline
# 이거 이해 제대로 못했음.. 나중에 짬 좀 채우고 다시 오자.
def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x] = True
    size = 1
    level[x] = lv
    for i in range(len(link[x])):
        next = link[x][i]
        size += dfs(next,lv + 1)
    tsize[x] = size
    return size


N = int(input())
link = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
level = [False] * (N + 1)
tsize = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
ans = list(map(int,input().split()))


if ans[0] != 1:
    print(0)
    exit()
else:
    dfs(1,0)
    for i in range(1,N):
        x = ans[i]
        if tsize[x] == 1 or i + tsize[x] >= N:
            continue
        next = ans[i + tsize[x]]
        if level[next] > level[x]:
            print(0)
            exit()
    print(1)

    
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