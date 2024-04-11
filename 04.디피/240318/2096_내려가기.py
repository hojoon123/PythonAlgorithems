import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    graph = list(map(int,input().split()))
    max_dp, min_dp = graph, graph
    
    for i in range(n-1):
        graph = list(map(int,input().split()))
        max_dp = [max(max_dp[0],max_dp[1]) + graph[0], max(max_dp) + graph[1], max(max_dp[1], max_dp[2]) + graph[2]]
        min_dp = [min(min_dp[0],min_dp[1]) + graph[0], min(min_dp) + graph[1], min(min_dp[1], min_dp[2]) + graph[2]]
    print(max(max_dp), min(min_dp))

if __name__ == '__main__':
    main()