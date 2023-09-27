import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(start, tree, root):
    for i in tree[start]:
        if root[i] == 0:
            root[i] = start
            dfs(i, tree, root)

if __name__ == '__main__':
    n = int(input())
    tree = [[] for i in range(n + 1)]
    root = [0 for i in range(n + 1)]
    
    for i in range(n - 1):
        a, b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    dfs(1, tree, root)
    
    for i in range(2, n + 1):
        print(root[i])
    
'''
예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
'''