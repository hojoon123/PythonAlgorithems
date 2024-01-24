import sys
import heapq
input = sys.stdin.readline

def solve(v,e, graph, distance, inf, start):
    distance[start] = 0
    
    for i in range(v):
        for j in range(e):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            
            if distance[cur] != inf and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                
                if i == v - 1:
                    return False
    return distance
    

def main():
    v, e = map(int,input().split())
    graph = []
    inf = int(1e9)
    for i in range(e):
        a, b, c = map(int,input().split())
        graph.append((a,b,c))
    distance = [inf for i in range(v + 1)]
    
    ans = solve(v,e, graph, distance, inf, 1)
    
    if not ans:
        print(-1)
    else:
        for i in range(2, v+1):
            if ans[i] == inf:
                print(-1)
            else:
                print(ans[i])
    
if __name__ == "__main__":
    main()
