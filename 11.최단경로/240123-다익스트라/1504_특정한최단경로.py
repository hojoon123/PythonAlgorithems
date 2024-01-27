import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start):
    distance = [int(1e9)] * (v + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        
        for next in graph[node]:
            n_node, n_dist = next[0], next[1] + distance[node]
            if distance[n_node] > n_dist:
                distance[n_node] = n_dist
                heapq.heappush(q, (n_dist, n_node))

    return distance

def main():
    v, e = map(int,input().split())
    graph = [[] for i in range(v + 1)]
    for i in range(e):
        a, b, c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    v1, v2 = map(int,input().split())
    distance = solve(v,graph, 1)
    a_distance = solve(v,graph, v1)
    b_distance = solve(v,graph, v2)
    
    v1_path = distance[v1] + a_distance[v2] + b_distance[v]
    v2_path = distance[v2] + b_distance[v1] + a_distance[v]
    
    ans = min(v1_path, v2_path)
    print(ans if ans < int(1e9) else -1)
    
if __name__ == "__main__":
    main()
