import sys
from collections import deque
import copy
input = sys.stdin.readline

def check(start, graph):
    x, y = start
    cur = graph[x][y]
    if x == 0:
        for i in range(1,n):
            if graph[i][y] > cur or (cur - graph[i][y]) >= 2:
                return 0
            if cur == graph[i][y]:
                flag = False
            if (cur - graph[i][y]) == 1:
                if flag:
                    return 0
                flag = True
        else:
            return 1
            
            
            
if __name__ == '__main__':
    n, l = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    cnt = 0
    # 0 0,  n-1 0,  0 n-1, n-1 n-1  
    for i in range(n):
        tmp_graph = copy.deepcopy(graph)
        cnt += check(i,tmp_graph)
    for i in range(n):
        tmp_graph = copy.deepcopy(graph)
        cnt += check(graph[0][i], tmp_graph)
        
        tmp_graph = copy.deepcopy(graph)
        cnt += check(graph[i][0], tmp_graph)
    