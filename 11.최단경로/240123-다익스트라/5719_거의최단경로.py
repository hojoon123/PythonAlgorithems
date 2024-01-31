import sys
import heapq
from collections import deque
input = sys.stdin.readline

def solve(v, graph, shorts, start):
    distance = [int(1e9) for i in range(v)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        
        for next in graph[node]:
            n_node, n_dist = next[0], next[1] + dist
            if shorts[node][n_node]:
                continue
            if distance[n_node] > n_dist:
                distance[n_node] = n_dist
                heapq.heappush(q, (n_dist, n_node))
                
    return distance

def bfs(distance, graph_inv, shorts, start, end):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        
        if node == end:
            continue
        for post_node, post_dist in graph_inv[node]:
            if post_dist + distance[post_node] == distance[node] and not shorts[post_node][node]:
                shorts[post_node][node] = True
                q.append(post_node)
    return shorts

def main():
    while 1:
        v, e = map(int,input().split())
        if v == 0:
            return
        
        start, end = map(int,input().split())
        graph = [[] for i in range(v)]
        graph_inv = [[] for i in range(v)]
        shorts = [[False] * v for i in range(v)]
        for i in range(e):
            a, b, c = map(int,input().split())
            graph[a].append((b,c))
            graph_inv[b].append((a,c))
            
        dist = solve(v, graph, shorts, start)
        shorts = bfs(dist, graph_inv, shorts, end, start)
        dist = solve(v, graph, shorts, start)
        print(dist[end] if dist[end] != int(1e9) else -1)
        
    
if __name__ == "__main__":
    main()