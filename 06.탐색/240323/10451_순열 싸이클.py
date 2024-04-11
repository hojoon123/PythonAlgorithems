import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
    visited[node] = 1
    n_node = graph[node]
    if not visited[n_node]:
        dfs(n_node)
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        graph = [0] + list(map(int,input().split()))
        visited =[1] + [0] * n
        ans = 0
        
        for i in range(1, n+1):
            if not visited[i]:
                dfs(i)
                ans += 1
                
        print(ans)