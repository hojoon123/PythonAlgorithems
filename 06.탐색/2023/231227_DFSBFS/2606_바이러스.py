from collections import deque
import sys
input = sys.stdin.readline

def solve(graph,v):
    cnt = 0
    q = deque()
    visited = [False for i in range(v+1)]
    
    visited[1] = True
    q.append(1)
    
    while q:
        virNode = q.popleft()
        
        for toNode in graph[virNode]:
            if not visited[toNode]:
                q.append(toNode)
                visited[toNode] = True
                cnt += 1
                
    return cnt
    
    

def main():
    v, e  = int(input()), int(input())
    graph = [[] for i in range(v+1)]
    for i in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(solve(graph, v))
    
    
        
if __name__ == "__main__":
    main()
    
'''
예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1 
4
'''