import sys
import heapq
from collections import deque
input = sys.stdin.readline

def solve(v, graph, start, k):
    distance = [[sys.maxsize for j in range(k+1)] for i in range(v+1)]
    cnt = 0
    distance[start][cnt] = 0
    q = []
    heapq.heappush(q, (0,start, cnt))
    
    while q:
        dist, node, cnt = heapq.heappop(q)
        if dist > distance[node][cnt]:
            continue
        
        for next in graph[node]:    
            n_node, n_dist = next[0], next[1] + dist
            if distance[n_node][cnt] > n_dist:
                distance[n_node][cnt] = n_dist
                heapq.heappush(q, (n_dist, n_node, cnt))
            
            if cnt < k and distance[n_node][cnt+1] > dist:
                distance[n_node][cnt+1] = dist
                heapq.heappush(q, (dist, n_node, cnt+1))
                
    return min(distance[v])

def main():
    v, e, k = map(int,input().split())
    graph = [[] for i in range(v+1)]
    for i in range(e):
        a, b, c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    print(solve(v, graph, 1, k))
        

  
if __name__ == "__main__":
    main()