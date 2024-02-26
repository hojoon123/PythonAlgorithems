import sys
input = sys.stdin.readline

def solve(graph, visited, qs):
    ans = sum(graph)
    print(ans)
    for q in qs:
        if q[0] == 2:
            idx = q[1]
            if not visited[idx]:
                ans -= graph[idx]
                visited[idx] = True
            else:
                ans += graph[idx]
                visited[idx] = False
        else:
            if not visited[q[1]]:
                ans += q[2] - graph[q[1]]
                graph[q[1]] = q[2]
            else:
                graph[q[1]] = q[2]
        print(ans)
def main():
    n = int(input())
    graph = list(map(int,input().split()))
    graph = [0] + graph
    visited = [0] * (n + 1)
    q = int(input())
    qs = []
    for i in range(q):
        s = list(map(int,input().split()))
        qs.append(s)
    solve(graph, visited, qs)
    
if __name__ == "__main__":
    main()