import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start,group):
    global ans

    if ans:
        return

    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[start] == visited[i]:
            ans = 1
            return


for k in range(int(input())):
    
    N,M = map(int,input().split())
    visited = [0] * (N + 1)
    graph = [[] for i in range(N+1)]
    ans = 0
    
    for _ in range(M): # 간선 입력
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i, 1)
            if ans:
                break
            
    if ans:
        print('NO')
    else:
        print('YES')
    print(graph)
#테스트 케이스가 있어서 exit 바로 못 때리니까 걍 bfs 돌리는게 더 빠를 수도
# 함해보자

'''
예제 입력 1 
2
--------
3 2

1 3
2 3

--------
4 4

1 2
2 3
3 4
4 2
예제 출력 1 
YES
NO
'''