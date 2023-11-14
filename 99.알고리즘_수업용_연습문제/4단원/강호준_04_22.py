import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 너비우선탐색
def bfs(v):
    q = deque()
    q.append(v)       
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(node[v], end = " ")
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

# 깊이우선탐색
def dfs(v):
    visit_list2[v] = 1        
    print(node[v], end = " ")
    for i in range(1, n + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)
            
if __name__ == "__main__": # 메인문입니다.
    # 직접 입력받기
    # n, m, v = map(int,input().split()) # 정점 / 간선 / 시작지점
    #graph = [[0] * (n + 1) for _ in range(n + 1)]
    # for _ in range(m):
    #     a, b = map(int, input().split())
    #     graph[a][b] = graph[b][a] = 1
    #visit_list = [0] * (n + 1)
    #visit_list2 = [0] * (n + 1)
    
    node = ['0','A','B','C','D','E','F','G','H']
    n, m, v = 8, 9, 1 # 노드 8개 간선 9개 시작지점 A
    graph = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,1,1,0,0,0,0,0],
                [0,1,0,0,1,0,0,0,0],
                [0,1,0,0,1,1,0,0,0],
                [0,0,1,1,0,0,1,0,0],
                [0,0,0,1,0,0,0,1,1],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0,1],
                [0,0,0,0,0,1,0,1,0]
            ]
    visit_list = [0] * (n + 1)
    visit_list2 = [0] * (n + 1)
    
    dfs(v)
    print()
    bfs(v)