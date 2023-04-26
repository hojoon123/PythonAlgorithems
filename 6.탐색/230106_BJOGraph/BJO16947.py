import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, idx, cnt):
    global cycle
    visited[idx] = 1
    
    for i in link[idx]:
        if visited[i] == 0:
            dfs(start, i, cnt + 1)
        elif i == start and cnt >= 2:
            cycle = True
            return
            
def bfs():
    global distance
    queue = deque()
     
    for i in range(N):
        if cycle_station[i] == True:
            distance[i] = 0
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        
        for i in link[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1
    print(*distance)
        
if __name__ == '__main__':
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

    bfs()
'''
dfs 로 먼저 순환역 체크 cnt >= 2 start == idx
bfs 로 역과 순환역 거리 체크 
순환선은 0으로 체크 후 방문 처리, 방문한 적이 없는 역들 방문하면서 +1 체
역의 개수 N(3 ≤ N ≤ 3,000)
간선 양방향

총 N개의 정수를 출력
1번 역과 순환선 사이의 거리, 2번 역과 순환선 사이의 거리,
..., N번 역과 순환선 사이의 거리를 공백으로 구분해 출력
예제 입력 1 
4
1 3
4 3
4 2
1 2
예제 출력 1 
0 0 0 0
'''