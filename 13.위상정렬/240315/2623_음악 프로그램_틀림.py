from collections import deque
import sys
input = sys.stdin.readline

def solve(n, m, link, cntlink, first_out):
    ans = []
    q = deque(first_out[1:])
    for i in range(1, n + 1):
        if cntlink[i] == 0:
            q.append(i)
    while q:
        cur_node = q.popleft()
        ans.append(cur_node)
        
        for to_node in link[cur_node]:
            cntlink[to_node] -= 1
            if cntlink[to_node] == 0:
                q.append(to_node)
    return ans
        
      

def main():
    n, m = map(int,input().split())
    link = [[] for i in range(n + 1)]
    cntlink = [0] * (n + 1)
    first_out = [0]
    for i in range(m):
        tmp = list(map(int,input().split()))
        first_out.append(tmp[1])
        for j in range(tmp[0], 0, -1):
            for to in tmp[1:j]:
                link[to].append(tmp[j])
                cntlink[tmp[j]] += 1
    
    for i in range(1, m + 1):
        for node in link[first_out[i]]:
            cntlink[node] -= 1
        link[first_out[i]] = []
        cntlink[first_out[i]] = -1

    print(solve(n, m, link, cntlink, first_out))
    
if __name__ == "__main__":
    main()