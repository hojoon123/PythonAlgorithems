import sys
import heapq
input = sys.stdin.readline

def solve(v, graph, inf, start):
    distance= [inf for i in range(v + 1)]
    distance[start] = 0
    for i in range(v):
        for j in range(len(graph)):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            
            if distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == v-1:
                    return True
    return False
    

def main():
    t = int(input())
    for _ in range(t):
        v, e, e2 = map(int,input().split())
        graph = []
        inf = int(1e9)
        for i in range(e):
            s, e, w = map(int,input().split())
            graph.append((s,e,w))
            graph.append((e,s,w))
        for i in range(e2):
            s, e, w = map(int,input().split())
            graph.append((s,e,-w))
            
        if solve(v, graph, inf, 1):
            print("YES")
        else:
            print("NO")

    
if __name__ == "__main__":
    main()
