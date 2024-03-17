import sys
from collections import Counter
input = sys.stdin.readline

def solve(graph):
    n = 10
    row = 1
    cow = 1
    for i in range(n):
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                row += 1
            else:
                row = 1
                break
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cow += 1
            else:
                cow = 1
                break
        if row == 10 or cow == 10:
            return 1
    
    return 0
    
def main():
    graph = [list(map(str, input().rstrip().split())) for i in range(10)]
    print(solve(graph))
    
    
if __name__ == "__main__":
    main()
