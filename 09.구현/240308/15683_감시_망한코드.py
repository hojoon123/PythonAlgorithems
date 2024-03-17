import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(graph, deaph, max_deaph, visited):
    global ans
    if deaph == max_deaph:
        tmp = 0
        for i in range(n):
            tmp += graph[i].count(0)
        if ans > tmp:
            ans = tmp
        print(tmp)
        return
    
    tmp_graph = copy.deepcopy(graph)

    for k in range(len(cctvs)):
        if visited[k] == False:
            visited[k] = True
            target, x, y = cctvs[k]

            if target != 5:
                # 이거 처리
                for i in range(4):
                    if target == 1:
                        if i == 0:
                            tmp_graph = build_right(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 1:
                            tmp_graph = build_down(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 2:
                            tmp_graph = build_left(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        else:
                            tmp_graph = build_up(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        for i in range(n):
                            print(*tmp_graph)
                        print()
                    elif target == 2:
                        if i % 2:
                            tmp_graph = build_right(tmp_graph, x, y)
                            tmp_graph = build_left(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        else:
                            tmp_graph = build_down(tmp_graph, x, y)
                            tmp_graph = build_up(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                    elif target == 3:
                        if i == 0:
                            tmp_graph = build_right(tmp_graph, x, y)
                            tmp_graph = build_down(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 1:
                            tmp_graph = build_down(tmp_graph, x, y)
                            tmp_graph = build_left(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 2:
                            tmp_graph = build_left(tmp_graph, x, y)
                            tmp_graph = build_up(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        else:
                            tmp_graph = build_up(tmp_graph, x, y)
                            tmp_graph = build_right(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                    else:
                        if i == 0:
                            tmp_graph = build_right(tmp_graph, x, y)
                            tmp_graph = build_down(tmp_graph, x, y)
                            tmp_graph = build_left(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 1:
                            tmp_graph = build_down(tmp_graph, x, y)
                            tmp_graph = build_left(tmp_graph, x, y)
                            tmp_graph = build_up(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        elif i == 2:
                            tmp_graph = build_left(tmp_graph, x, y)
                            tmp_graph = build_up(tmp_graph, x, y)
                            tmp_graph = build_right(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                        else:
                            tmp_graph = build_up(tmp_graph, x, y)
                            tmp_graph = build_right(tmp_graph, x, y)
                            tmp_graph = build_down(tmp_graph, x, y)
                            check(tmp_graph, deaph + 1, max_deaph, visited)
                    
                    
            else: # 다 바꿔야 할 때
                tmp_graph = build_right(tmp_graph, x, y)
                tmp_graph = build_left(tmp_graph, x, y)
                tmp_graph = build_up(tmp_graph, x, y)
                tmp_graph = build_down(tmp_graph, x, y)
                check(tmp_graph, deaph + 1, max_deaph, visited)

            visited[k] = False
    

def build_right(graph, x, y):
    for i in range(y, m):
        if graph[x][i] == 0:
            graph[x][i] = "#"
        elif graph[x][i] == 6:
            break
    return graph

def build_left(graph, x, y):
    for i in range(0, y):
        if graph[x][i] == 0:
            graph[x][i] = "#"
        elif graph[x][i] == 6:
            break
    return graph

def build_up(graph, x, y):
    for i in range(0, x):
        if graph[i][y] == 0:
            graph[i][y] = "#"
        elif graph[i][y] == 6:
            break
    return graph

def build_down(graph, x, y):
    for i in range(x, n):
        if graph[i][y] == 0:
            graph[i][y] = "#"
        elif graph[i][y] == 6:
            break
    return graph

if __name__ == '__main__':
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],                    
    [[0, 1], [1, 2], [2, 3], [3, 0]],    
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
    ]

    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    cctvs =  []
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and graph[i][j] != 6:
                cctvs.append((graph[i][j],i,j))
            elif graph[i][j] == 0:
                ans += 1
    visited = [False for i in range(len(cctvs))]
    check(graph, 0, len(cctvs), visited)
    print(ans)
