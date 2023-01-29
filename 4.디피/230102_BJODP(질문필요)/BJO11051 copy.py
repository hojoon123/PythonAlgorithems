import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#솔직히 코드 이해가 잘 안됩니다. 트리가 안 그려져요....
def choose(times, got):
    if times == N:
        return got == K

    if graph[times][got] != -1:
        return graph[times][got]

    graph[times][got] = choose(times+1, got) + choose(times+1, got+1)
    return graph[times][got]

N, K = map(int,input().split())
graph = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
print(choose(0,0) % 10007)
'''
\(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007
예제 입력 1 
5 2
예제 출력 1 
10
'''