import sys
import heapq
input = sys.stdin.readline

def kruskal(adj):
    
    w_sum = 0
    for node_a, node_b, edge_cost in adj:
        a_root = find(node_a)
        b_root = find(node_b)
        if a_root != b_root:
            if a_root > b_root:
                v_root[a_root] = b_root
            else:
                v_root[b_root] = a_root
            w_sum += edge_cost
                
    return w_sum

def find(node):
    if node != v_root[node]:
        v_root[node] = find(v_root[node])
    return v_root[node]

if __name__ == "__main__":
    v, edge = map(int,input().split())
    adj=[]
    v_root = [i for i in range(v+1)]
    for i in range(edge):
        adj.append(list(map(int,input().split())))
    
    adj.sort(key=lambda x:x[2])
        
    print(kruskal(adj))