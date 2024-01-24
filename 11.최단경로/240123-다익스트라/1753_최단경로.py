import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start):
    distance = [float("INF") for i in range(v + 1)]
    distance[start] = 0 
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        
        for nx in graph[node]:
            n_node, n_dist = nx[0], nx[1] + distance[node]
            if n_dist < distance[n_node]:
                distance[n_node] = n_dist
                heapq.heappush(q,(n_dist, n_node))
                
    for i in range(1, len(distance)):
        if distance[i] == float("INF"):
            print("INF")
        else:
            print(distance[i])

def main():
    v, e = map(int,input().split())
    start = int(input())
    graph = [[] for i in range(v + 1)]
    for i in range(e):
        a, b, w = map(int,input().split())
        graph[a].append((b, w))

    solve(v, graph, start)
    
if __name__ == "__main__":
    main()
