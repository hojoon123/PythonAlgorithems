import sys
input = sys.stdin.readline

def solve(graph, v):
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v +  1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                
    return graph

def main():
    v, e = map(int,input().split())
    graph = [[0] * (v + 1) for i in range(v + 1)]
        
    for i in range(e):
        start, end = map(int,input().split())
        graph[start][end] = 1
        
    students = solve(graph, v)   
    ans = 0
        
    for i in range(1, v + 1):
        check = 0
        for j in range(1, v + 1):
            check += students[i][j] + students[j][i]
            
        if check == (v - 1):
            ans += 1
    print(ans)
    for i in range(len(students)):
        print(*students[i])
    
if __name__ == "__main__":
    main()
