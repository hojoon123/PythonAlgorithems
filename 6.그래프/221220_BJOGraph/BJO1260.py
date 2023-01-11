from sys import stdin
from collections import deque
input = stdin.readline
#BFS DFS 기초가 되는 최고의 문제
def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, N + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
    visit_list2[v] = 1
    print(v, end = " ")
    for i in range(1, N + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

N, M, V = map(int,input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visit_list = [0] * (N + 1)
visit_list2 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
  
dfs(V)
print()
bfs(V)

'''
정점의 개수 N(1 ≤ N ≤ 1,000)
간선의 개수 M(1 ≤ M ≤ 10,000)
시작할 정점의 번호 V
 두 정점의 번호
 
예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
'''