import sys
from collections import deque
input = sys.stdin.readline
        
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        v_root[y] = x
    else:
        v_root[x] = y
        
def find(node):
    if node != v_root[node]:
        v_root[node] = find(v_root[node])
    return v_root[node]
    
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    v_root = [i for i in range(n+1)]
    for i in range(1,n+1):
        arr = list(map(int,input().split()))
        for j in range(n):
            if arr[j] == 1:
                union(i,j+1)
    
    path = list(map(int,input().split()))
    s = v_root[path[0]]
    for i in range(1,m):
        if v_root[path[i]] != s:
            print("NO")
            break
    else:
        print("YES")