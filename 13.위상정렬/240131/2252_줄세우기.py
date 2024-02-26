from collections import deque
import sys
input = sys.stdin.readline

def solve(n, m, graph, cnt):
    q = deque()
    tmp = []
    for i in range(1,n+1):
        if cnt[i] == 0:
            q.append(i)
            tmp.append(i)
    while q:
        node = q.popleft()
        for n_node in graph[node]:
            cnt[n_node] -= 1
            if cnt[n_node] == 0:
                q.append(n_node)
                tmp.append(n_node)
    
    return tmp
            
def main():
    n, m = map(int,input().split())
    graph = [[] for i in range(n+1)]
    cnt = [0 for i in range(n+1)]
    
    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        cnt[b] += 1
    
    ans = solve(n, m, graph, cnt)
    print(*ans)
        
if __name__ == "__main__":
    main()