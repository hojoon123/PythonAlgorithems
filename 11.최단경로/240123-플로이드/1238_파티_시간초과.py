import sys
import heapq
input = sys.stdin.readline

def solve(v, graph):
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

def main():
    v, e ,x = map(int,input().split())
    inf = int(1e9)
    graph = [[inf] * (v + 1) for i in range(v + 1)]
    for i in range(1, v + 1):
        graph[i][i] = 0
    for i in range(e):
        a, b, c = map(int,input().split())
        graph[a][b] = c
    
    graph = solve(v, graph)
    ans = []
    for i in range(1, v+1):
        ans.append(graph[i][x] + graph[x][i])
    print(max(ans))
    
if __name__ == "__main__":
    main()
