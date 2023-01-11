import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, depth):
    visited[v] = 1
    if depth == 4:
        print(1)
        exit()
    
    for i in relations[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0

N,M = map(int,input().split())
visited = [0] * (N + 1)
relations = [[] for i in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    relations[a].append(b)
    relations[b].append(a)

for i in range(N):
    dfs(i,0)
    visited[i] = 0
    
print(0)

'''
사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)
M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구

예제 입력 1 
5 4
0 1
1 2
2 3
3 4
예제 출력 1 
1
'''