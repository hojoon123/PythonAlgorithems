from collections import deque
import sys
input = sys.stdin.readline

def solve(n, link, cntlink, costs):
    dp = [0 for i in range(n + 1)]
    q = deque()
    
    for i in range(1, n + 1):
        if cntlink[i] == 0:
            q.append(i)
            dp[i] = costs[i]
    
    while q:
        cur = q.popleft()
        for to_node in link[cur]:
            cntlink[to_node] -= 1
            dp[to_node] = max(dp[to_node], dp[cur] + costs[to_node])
            if cntlink[to_node] == 0:
                q.append(to_node)
                
    return dp
        
def main():
    n = int(input())
    link = [[] for i in range(n+1)]
    cntlink = [0] *(n + 1)
    costs = [0]
    
    for i in range(1, n + 1):
        house = list(map(int,input().split()))
        costs.append(house[0])

        if house[1] == -1:
            continue
        
        for j in house[1:-1]:
            link[j].append(i)
            cntlink[i] += 1
    
    for i in solve(n, link, cntlink, costs)[1:]:
        print(i)

if __name__ == "__main__":
    main()