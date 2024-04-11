import sys
from collections import deque
input = sys.stdin.readline
                    
def solve():
    dead = deque()
    ans = 0
    
    for _ in range(k):
        for i in range(n): #봄
            for j in range(n):
                if len(graph[i][j]) == 1:
                    continue
                elif len(graph[i][j]) == 2: # 나무 1개 있을 때
                    if graph[i][j][0] >= graph[i][j][1]:
                        graph[i][j][0] -= graph[i][j][1]
                        graph[i][j][1] += 1
                    else:
                        dead.append([i,j,graph[i][j].pop()])
                
                elif graph[i][j][0] == 0:
                    for q in range(len(graph[i][j][1:])):
                        dead.append(graph[i][j].pop())
                        
                else: # 나무 2개 이상일 때
                    for young_tree in sorted(graph[i][j][1:]):
                        if graph[i][j][0] >= young_tree:
                            graph[i][j][0] -= young_tree
                            tmp = [-1] + graph[i][j][1:]
                            idx = tmp.index(young_tree)
                            graph[i][j][idx] += 1
                        else:
                            dead.append([i,j,graph[i][j].pop(graph[i][j].index(young_tree))])
                            
        while dead: # 여름
            x, y, age = dead.pop()
            graph[x][y][0] += age // 2
        
        for i in range(n): # 가을
            for j in range(n):
                graph[i][j][0] += fertilizers[i][j] # 겨울
                
                if len(graph[i][j]) == 1:
                    continue
                else: 
                    for tree_age in graph[i][j][1:]:
                        if tree_age % 5 == 0:
                            for q in range(8):
                                nx = i + dx[q]
                                ny = j + dy[q]
                                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                    continue
                                graph[nx][ny].append(1)
    
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 1:
                ans += len(graph[i][j]) - 1
    return ans
        
if __name__ == "__main__":
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    n, m, k = map(int,input().split())
    graph = [[[5] for j in range(n)] for i in range(n)]
    fertilizers = [list(map(int,input().split())) for i in range(n)]

    for i in range(m):
        x, y, age = list(map(int,input().split()))
        graph[x-1][y-1].append(age)
        
    print(solve())