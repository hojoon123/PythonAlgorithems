import sys
from collections import deque
input = sys.stdin.readline

def magic(n, graph, line):
    cnt = 0
    if line == 'r':
        for i in range(n):
            cur = 0
            for j in range(n):
                if graph[i][j] == '.':
                    graph[i][j] = ','
                    cur += 1
                if graph[i][j] == 'X' or j == (n - 1):
                    if cur >= 2:
                        cnt += 1
                        cur = 0
                    else:
                        cur = 0
                
    else:
        for i in range(n):
            cur = 0
            for j in range(n):
                if graph[j][i] == '.' or graph[j][i] == ',':
                    graph[j][i] = ';'
                    cur += 1
                if graph[j][i] == 'X' or j == (n - 1):
                    if cur >= 2:
                        cnt += 1
                        cur = 0
                    else:
                        cur = 0
    return cnt
                
    
def main():
    n = int(input())
    graph = [list(map(str,input().rstrip())) for i in range(n)]
    r = magic(n, graph, 'r')
    c = magic(n, graph, 'c')
    print(r, c)
    
if __name__ == "__main__":
    main()