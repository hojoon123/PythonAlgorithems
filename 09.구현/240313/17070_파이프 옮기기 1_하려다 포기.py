import sys
from collections import deque
input = sys.stdin.readline

# 확산
def solve(n, graph, pipe):
    dp = [[0 for i in range(n)] for j in range(n)]
    modes = [
        [([0,1],[0,1]),([0,1],[1,1])], # 가로 0 
        [([1,0],[1,0]),([1,0],[1,1])], # 세로 1 
        [([1,1],[1,1]),([1,1],[0,1]),([1,1],[1,0])] # 대각 2
    ]
    q = deque()
    q.append(pipe)
    
    while q:
        state, pipe = q.popleft()
        
        for mode in modes[state]:
            nx = pipe[0] + mode[0]
            ny = pipe[1] + mode[1]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 1:
                continue
            
            
            

def main():
    n = int(input())
    graph = [list(map(int,input().split())) for i in range(n)]
    solve(n, graph,(0,[0,0],[0,1]))

if __name__ == '__main__':
    main()