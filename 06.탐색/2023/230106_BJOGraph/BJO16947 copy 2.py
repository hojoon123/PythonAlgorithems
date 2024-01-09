from BJO16947 import dfs


N = int(input())
link = [[] for i in range(N)]
cycle_station = [0] * N # 순환역
distance = [-1] * N # 순환역으로부터의 거리

for i in range(N):
    a, b = map(int,input().split())
    link[a - 1].append(b - 1)
    link[b - 1].append(a - 1)

for i in range(N):
    visited = [0] * N
    cycle = False
    
    dfs(i, i, 0)
    
    if cycle:
        cycle_station[i] = 1
print(cycle_station)