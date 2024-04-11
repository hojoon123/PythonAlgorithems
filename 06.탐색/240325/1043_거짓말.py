import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def get_true_nodes(true_nodes):
    q = deque(true_nodes)
    visited = [0] * (n+1)
    
    while q:
        x = q.popleft()
        visited[x] = 1

        for n_node in graph[x]:
            if visited[n_node] == 0:
                q.append(n_node)
                true_nodes.add(n_node)
                
    return true_nodes

if __name__ == '__main__':
    n, m = map(int,input().split())
    true_nodes = list(map(int,input().split()))
    if len(true_nodes) == 1:
        print(m)
        exit()
    else:
        true_nodes.pop(0)
        
    graph = [set() for i in range(n+1)]
    partys = []
    for i in range(1,m+1):
        party = list(map(int,input().split()))
        partys.append(party[1:])
        for node in party[1:]:
            graph[node].update(party[1:])
    
    for i in range(1,n+1):
        graph[i].discard(i)

    true_nodes = get_true_nodes(set(true_nodes))
    ans = 0
    
    for party in partys:
        for target in party:
            if target not in true_nodes:
                ans += 1
                break
    print(ans)