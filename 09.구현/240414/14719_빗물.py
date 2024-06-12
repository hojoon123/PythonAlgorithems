import sys
from collections import deque
input = sys.stdin.readline
                    
def solve():
    ans = 0
    
    for i in range(1, m - 1):
        left_max = max(graph[:i])
        right_max = max(graph[i+1:])

        compare = min(left_max, right_max)

        if graph[i] < compare:
            ans += compare - graph[i]

    return ans
        
if __name__ == "__main__":
    n, m = map(int,input().split())
    graph = list(map(int,input().split()))
    print(solve())