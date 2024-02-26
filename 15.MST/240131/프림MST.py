import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, visited, start):
    q = []
    heapq.heappush(q, (0,start))
    ans = 0
    cnt = 0

    while q:
        if cnt == v:
            break
        node, cost = heapq.heappop(q)
        if not visited[node]:
            visited[node] = True
            cnt += 1
            ans += cost
            for n_node, n_cost in graph[node]:
                heapq.heappush(q, (n_node, n_cost))
                
    return ans

if __name__ == "__main__":
    v, e = map(int,input().split())
    graph=[[] for n in range(v+1)]
    visited = [False for _ in range(v+1)]
    for i in range(e):
        a, b, cost = map(int,input().split())
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    
        
    print(prim(v, graph, visited, 1))