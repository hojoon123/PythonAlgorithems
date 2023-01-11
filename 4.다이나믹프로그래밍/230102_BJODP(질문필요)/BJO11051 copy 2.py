import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def choose(times, left):
    if times == 0:
        return left == 0

    if graph[times][left] != -1:
        return graph[times][left]

    graph[times][left] = choose(times-1, left) + choose(times-1, left-1)
    return graph[times][left]

N, K = map(int,input().split())
graph = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
print(choose(N,K) % 10007)
'''
\(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007
예제 입력 1 
5 2
예제 출력 1 
10
'''