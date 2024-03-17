import sys
import heapq
input = sys.stdin.readline

# 마을 2개로 나누기 MST -> 제일 긴 간선 재끼면 마을 2개
def kruskal(graph):
    ans = 0
    last_edge = 0
    for a, b, cost in graph:
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            if a_root > b_root:
                v_root[a_root] = b_root
            else:
                v_root[b_root] = a_root
            ans += cost
            last_edge = cost
    ans -= last_edge
    return ans

def find(node):
    if node != v_root[node]:
        v_root[node] = find(v_root[node])
    return v_root[node]

if __name__ == "__main__":
    v, e = map(int,input().split())
    graph=[]
    v_root = [i for i in range(v+1)]
    for i in range(e):
        graph.append(list(map(int,input().split())))
    
    graph.sort(key=lambda x:x[2])
    print(kruskal(graph))