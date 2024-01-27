import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start):
    distance = [int(1e9) for i in range(v + 1)]
    distance[start] = 0 
    pre_node = [0 for i in range(v + 1)]
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
                pre_node[n_node] = node
                heapq.heappush(q,(n_dist, n_node))
    return (distance, pre_node)

def main():
    v = int(input())
    e = int(input())
    graph = [[] for i in range(v + 1)]
    for i in range(e):
        a, b, w = map(int,input().split())
        graph[a].append((b, w))
    start, end = map(int,input().split())
    

    distance, pre_node = solve(v, graph, start)
    
    ans = distance[end]
    arr = [end]
    now = end
    while now != start:
        now = pre_node[now]
        arr.append(now)
    print(ans)
    print(len(arr))
    print(*arr[::-1])
    
if __name__ == "__main__":
    main()
