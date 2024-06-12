import sys
from collections import deque
input = sys.stdin.readline

def magic():
    pass
    
def main():
    n, m, k = map(int,input().split())
    graph = [[[] for i in range(n)] for j in range(n)]
    fire_balls = deque()
    for i in range(m):
        r, c, v, s, d = map(int,input().split())
        fire_balls.append([r-1,c-1,v,s,d])
        
    print(magic(graph, fire_balls, n, k))
        
if __name__ == "__main__":
    main()
    