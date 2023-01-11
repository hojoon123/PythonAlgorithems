from sys import stdin

input = stdin.readline

def func(n, k):
    graph = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][0] = 1
    for i in range(k + 1):
        graph[i][i] = 1

    print(graph)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            graph[i][j] = graph[i - 1][j] + graph[i - 1][j - 1]
    print(graph)
            
    return graph[n][k]
N, K = map(int,input().split())

print(func(N, K) % 10007)

'''
\(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007
예제 입력 1 
5 2
예제 출력 1 
10
'''