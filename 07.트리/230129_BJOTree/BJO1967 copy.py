import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(root, biase): # 트리 돌면서 root 로부터의 거리 체크
    
    for i in tree[root]:
        idx, next_biase = i
        
        if dist[idx] == -1:
            dist[idx] = biase + next_biase
            dfs(idx, dist[idx])
    

if __name__ == '__main__':
    n = int(input())
    tree = [[] for i in range(n + 1)]
    dist = [-1] * (n + 1)
    for i in range(n - 1):
        root, child, biase = map(int,input().split())
        tree[root].append([child, biase])
        tree[child].append([root,biase])
    
    dist[1] = 0
    dfs(1, 0)
    
    node = dist.index(max(dist))
    dist = [-1] * (n + 1)
    dist[node] = 0
    dfs(node, 0)
    
    print(max(dist))
    
    
    
'''
예제 입력 1 
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

예제 출력 1 
45
'''