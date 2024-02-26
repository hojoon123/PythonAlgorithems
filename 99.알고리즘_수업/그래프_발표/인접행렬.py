import sys
input = sys.stdin.readline

def mollu():
    pass

if __name__ == "__main__":
    
    graph = [[0] * 100000000 for _ in range(100000000)]
    graph[0][1], graph[0][5] = 1, 1