import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start):
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
            n_node, n_dist = next[0], distance[node] + next[1]
            if distance[n_node] > n_dist:
                distance[n_node] = n_dist
                heapq.heappush(q, (n_dist, n_node))
    return distance

def main():
    v, e ,x = map(int,input().split())
    graph = [[] for i in range(v + 1)]
    dist = [0 for i in range(v + 1)]
    for i in range(e):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))
    
    for i in range(1, v + 1):
        if i != x:
            # 시작 지점 기준 x 도착 시간 삽입
            dist[i] = solve(v, graph, i)[x]
        else:
            return_dist = solve(v, graph, x)
    for i in range(1, v + 1):
        return_dist[i] += dist[i]
    print(max(return_dist[1:]))
            
    
if __name__ == "__main__":
    main()
