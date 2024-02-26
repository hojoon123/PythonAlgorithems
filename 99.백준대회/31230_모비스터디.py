import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, v):
    inf = int(1e15)
    distance = [inf for i in range(v + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
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
    v, e, start, end = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))


    a_distance = dijkstra(start, graph, v)
    b_distance = dijkstra(end, graph, v)
    
    ans = a_distance[end]
    arr = []
    for i in range(1, v+1):
        if a_distance[i] + b_distance[i] == ans:
            arr.append(i)
    print(len(arr))
    print(*arr)

if __name__ == "__main__":
    main()
