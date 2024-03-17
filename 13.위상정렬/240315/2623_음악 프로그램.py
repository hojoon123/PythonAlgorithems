from collections import deque
import sys
input = sys.stdin.readline

def solve(n, link, cntlink):
    q= deque()
    ans = []
    for i in range(1, n+1):
        if cntlink[i] == 0:
            q.append(i)

    while q:
        cur_node = q.popleft()
        ans.append(cur_node)
        
        for i in link[cur_node]:
            cntlink[i] -= 1

            if cntlink[i] == 0:
                q.append(i)

    if len(ans) != n:
        return [0]
    else:
        return ans
        
def main():
    n, m = map(int,input().split())
    link = [[] for i in range(n + 1)]
    cntlink = [0] * (n + 1)
    
    for _ in range(m):
        arr = list(map(int, input().split()))
        for i in range(1, arr[0]):
            link[arr[i]].append(arr[i + 1])
            cntlink[arr[i + 1]] += 1

    ans = solve(n, link, cntlink)
    for i in ans:
        print(i)

if __name__ == "__main__":
    main()