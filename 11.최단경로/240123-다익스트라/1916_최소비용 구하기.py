import sys
import heapq
input = sys.stdin.readline

def solve(v, start, end, graph):
    inf = int(1e9)
    distance = [inf for i in range(v+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        
        for next in graph[node]:
            n_node = next[0]
            n_dist = next[1] + distance[node]
            if distance[n_node] > n_dist:
                distance[n_node] = n_dist
                heapq.heappush(q, (n_dist, n_node))
    return distance[end]
    
    

def main():
    v = int(input())
    e = int(input())
    inf = int(1e9)
    graph = [[] for i in range(v+1)]
    for _ in range(e):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))
    start, end = map(int,input().split())
    
    print(solve(v, start, end, graph))
    
    
if __name__ == "__main__":
    main()
