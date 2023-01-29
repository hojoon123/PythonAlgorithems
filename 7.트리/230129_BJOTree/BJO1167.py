import sys
from collections import deque
input = sys.stdin.readline


def bfs(root): # 트리 돌면서 root 로부터의 거리 체크
    dist = [-1] * (n + 1)
    q = deque()
    q.append(root)
    dist[root] = 0
    max = [0, 0] # 제일 먼 거리, node
    
    while q:
        x = q.popleft()
        
        for idx, biase in tree[x]:
            if dist[idx] == -1:
                dist[idx] = dist[x] + biase
                q.append(idx)
                
                if dist[idx] > max[0]:
                    max = dist[idx], idx
    
    return max
    

if __name__ == '__main__':
    n = int(input())
    tree = [[] for i in range(n + 1)]
    for i in range(n):
        arr = list(map(int,input().split()))
        for j in range(1, len(arr) - 2, 2):
            tree[arr[0]].append([arr[j], arr[j + 1]])
    
    ans, node = bfs(1)
    ans, node = bfs(node)
    print(ans)

'''
예제 입력 1 
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1 
11
'''