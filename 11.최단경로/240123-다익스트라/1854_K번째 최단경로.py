import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start, k):
    distance = [[] for i in range(v+1)]
    q = []
    heapq.heappush(q, (0,start))
    heapq.heappush(distance[start], 0)
    
    while q:
        dist, node = heapq.heappop(q)
        
        for next in graph[node]:
            n_node, n_dist = next[0], next[1] + dist
            
            if len(distance[n_node]) <= k:
                heapq.heappush(q, (n_dist, n_node))
                heapq.heappush(distance[n_node], -n_dist)
            else:
                if distance[n_node][0] < -n_dist:
                    heapq.heappop(distance[n_node])
                    heapq.heappush(q,(n_dist, n_node))
                    heapq.heappush(distance[n_node], -n_dist)

    return distance

def main():
    v, e, k = map(int,input().split())
    graph = [[] for i in range(v + 1)]
    for i in range(e):
        a, b, c = map(int,input().split())
        graph[a].append((b,c))
        
    dist = solve(v, graph, 1, k)
    for i in range(1, v+1):
        if len(dist[i]) < k:
            print(-1)
        else:
            dist[i].sort()
            print(-dist[i][-k])
    
if __name__ == "__main__":
    main()