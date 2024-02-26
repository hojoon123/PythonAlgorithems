import sys
import heapq
input = sys.stdin.readline

def kruskal(graph):
    ans = 0
    for a, b, cost in graph:
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            if a_root > b_root:
                v_root[a_root] = b_root
            else:
                v_root[b_root] = a_root
            ans += cost
            # 안 해도 되는거지만 굳이굳이 추가 노드의 개수가 적을 땐 유용할듯?
            # for i in range(1, v+1):
            #     if v_root[i] != 1:
            #         break
            # else:
            #     return ans
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