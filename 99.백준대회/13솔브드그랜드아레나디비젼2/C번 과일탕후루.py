import sys
from collections import deque
input = sys.stdin.readline

def solve(cnt, graph, fruits):
    while cnt > 2:
        if fruits[graph[0]] > fruits[graph[-1]]:
            idx = graph.pop()
        else:
            idx = graph.popleft()
            
        fruits[idx] -= 1
        if fruits[idx] == 0:
            cnt -= 1
    return len(graph)

def main():
    n = int(input())
    graph = deque(map(int,input().split()))
    fruits = {}
    for i in graph:
        if i in fruits:
            fruits[i] += 1
        else:
            fruits[i] = 1
    print(solve(len(fruits), graph, fruits))
    
    
if __name__ == "__main__":
    main()