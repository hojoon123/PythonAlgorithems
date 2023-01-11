import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v):
    if visited[v] > 0:
        return
    
    visited[v] = 1
    for i in link[v]:
        dfs(i)

N,M = map(int,input().split())
visited = [0] * N
link = [[] for i in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    link[a-1].append(b-1)
    link[b-1].append(a-1)

cnt = 0
for i in range(N):
    if visited[i] == 0:
        cnt += 1
        dfs(i)
print(cnt)
'''
정점의 개수 N(1 ≤ N ≤ 1,000)
간선의 개수 M(1 ≤ M ≤ 10,000)
시작할 정점의 번호 V
 두 정점의 번호
 
예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
'''