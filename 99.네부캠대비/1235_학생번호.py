import sys
from collections import deque
input = sys.stdin.readline

def magic(n, graph):
    len_s = len(graph[0])
    d = dict()
    for k in range(len_s - 1, -1, -1):
        d.clear()
        for i in range(n):
            tmp = graph[i][k:len_s]
            if ''.join(tmp) not in d:
                d[''.join(tmp)] = 1
            else:
                break
        else:
            return (len_s - k)
                
    
def main():
    n = int(input())
    graph = [list(map(str,input().rstrip())) for i in range(n)]
    ans = magic(n, graph)
    print(ans)
    
if __name__ == "__main__":
    main()