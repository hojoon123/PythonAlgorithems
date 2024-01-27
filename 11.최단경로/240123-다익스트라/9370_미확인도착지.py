import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, start):
    distance = [int(1e9) for i in range(v + 1)]
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
                
    return distance

def main():
    for i in range(int(input())):
        v, e, t = map(int,input().split())
        s, v1, v2 = map(int,input().split())
        graph = [[] for i in range(v+1)]
        for i in range(e):
            a, b, c = map(int,input().split())
            if (a == v1 and b == v2) or (a == v2 and b == v1):
                check = c
            graph[a].append((b,c))
            graph[b].append((a,c))
        targets = []
        for i in range(t):
            targets.append(int(input()))
            
        distance = solve(v, graph, s)
        v1_distance = solve(v, graph, v1)
        v2_distance = solve(v, graph, v2)
        ans = []
        
        for target in targets:
            tmp1 = check + distance[v1] + v2_distance[target]
            tmp2 = check + distance[v2] + v1_distance[target]
            if distance[target] == tmp1 or distance[target] == tmp2:
                ans.append(target)

        ans.sort()
        print(*ans)
    
    
if __name__ == "__main__":
    main()