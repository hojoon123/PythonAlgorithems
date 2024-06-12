import sys
from collections import Counter
input = sys.stdin.readline

def sort_new(graph, RC):
    sorted_graph = []
    max_cnt = 0
    
    for i in range(len(graph)):
        tmp = []
        dic = Counter(graph[i])
                
        for key,value in dic.items():
            if key == 0:
                continue
            tmp.append([key, value])
            
        tmp.sort(key=lambda x: [x[1], x[0]])
        
        tmp = sum(tmp,[])
        max_cnt = max(max_cnt, len(tmp))
        sorted_graph.append(tmp)
        
    for i in sorted_graph:
        i += [0] * (max_cnt - len(i))
        if len(i) > 100:
            i = i[:100]
            
    return sorted_graph if RC=="R" else list(zip(*sorted_graph))
        
if __name__ == "__main__":
    n, m, k = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(3)]
    cnt = 0
    while cnt <= 100:
        if n - 1 < len(graph) and m - 1 < len(graph[0]):
            if graph[n - 1][m - 1] == k:
                break
            
        # R 연산
        if len(graph) >= len(graph[0]):
            graph = sort_new(graph, "R")
            
        # C 연산
        else:
            graph = sort_new(list(zip(*graph)), "C")
        
        cnt += 1

    print(-1 if cnt == 101 else cnt)