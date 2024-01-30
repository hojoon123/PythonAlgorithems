import sys
import heapq
input = sys.stdin.readline

def solve(graph, v):
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v +  1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    return graph

def main():
    v, e = map(int,input().split())
    graph = [[0] * (v+1) for i in range(v+1)]
    for i in range(e):
        s, e = map(int,input().split())
        graph[s][e] = 1
        graph[e][s] = -1
    
    ans = solve(graph, v)
    k = int(input())
    for i in range(k):
        s, e = map(int,input().split())
        print(-ans[s][e])
    
if __name__ == "__main__":
    main()
