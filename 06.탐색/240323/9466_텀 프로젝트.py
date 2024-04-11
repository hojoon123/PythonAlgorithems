import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
    global ans
    visited[node] = 1
    cycle.append(node)
    n_node = graph[node]
    
    if not visited[n_node]:
        dfs(n_node)
    else:
        if n_node in cycle:
            ans += cycle[cycle.index(n_node):]
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        graph = [0] + list(map(int,input().split()))
        visited =[1] + [0] * n
        ans = []
        
        for i in range(1, n+1):
            if not visited[i]:
                cycle = []
                dfs(i)
                
        print(n - len(ans))