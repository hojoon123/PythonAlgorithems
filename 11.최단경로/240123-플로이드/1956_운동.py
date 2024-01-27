import sys
input = sys.stdin.readline

def solve(graph, v):
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v +  1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
                
    return graph

def main():
    v, e = map(int,input().split())
    graph = [[int(1e9)] * (v + 1) for i in range(v + 1)]
    for i in range(1, v + 1):
        graph[i][i] = 0
        
    for i in range(e):
        start, end, w = map(int,input().split())
        graph[start][end] =  w
    
    graph = solve(graph, v)   
    arr = []
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] and graph[j][i]:
                tmp = graph[i][j] + graph[j][i]
                if tmp < int(1e9):
                    arr.append(tmp)
    if arr:
        print(min(arr))
    else:
        print(-1)
    
if __name__ == "__main__":
    main()