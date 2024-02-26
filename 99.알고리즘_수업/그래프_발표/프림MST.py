import sys
import heapq
input = sys.stdin.readline

def prim(v, adj, visited):
    q = [[0,1]]
    w_sum = 0
    cnt = 0

    while q:
        if cnt == v:
            break
        now_cost,now_nodeB = heapq.heappop(q)
        if not visited[now_nodeB]:
            visited[now_nodeB] = True
            cnt += 1 
            w_sum += now_cost
            for next_info in adj[now_nodeB]:
                heapq.heappush(q, next_info)
                
    return w_sum

if __name__ == "__main__":
    v, edge = map(int,input().split())
    adj=[[] for n in range(v+1)]
    visited = [False for _ in range(v+1)]
    for i in range(edge):
        node_a, node_b, edge_cost = map(int,input().split())
        adj[node_a].append((edge_cost,node_b))
        adj[node_b].append((edge_cost,node_a))
    
        
    print(prim(v, adj, visited))