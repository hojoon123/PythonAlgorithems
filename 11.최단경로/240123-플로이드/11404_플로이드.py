import sys
import heapq
input = sys.stdin.readline

def solve(graph, v):
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v +  1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
                
    return graph

def main():
    v = int(input())
    e = int(input())
    inf = 10**7
    graph = [[inf] * (v + 1) for i in range(v + 1)]
    for i in range(1, v + 1):
        graph[i][i] = 0
        
    for i in range(e):
        start, end, w = map(int,input().split())
        graph[start][end] = min(graph[start][end], w)
        
    ans = solve(graph, v)   
    
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if ans[i][j] == inf:
                ans[i][j] = 0
        print(*ans[i][1:], sep= ' ')
    
if __name__ == "__main__":
    main()
