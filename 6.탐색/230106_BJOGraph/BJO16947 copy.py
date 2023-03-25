import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(idx, cnt):
    if cycle_station[idx]:
        if cnt - distance[idx] >= 3:
            return idx
        else: return -1
        
    cycle_station[idx] = 1
    distance[idx] = cnt
    
    for y in link[idx]:
        cycleStartNode = dfs(y, cnt + 1)
        
        if cycleStartNode != -1:
            cycle_station[idx] = 2
            if idx == cycleStartNode: return -1
            else: return cycleStartNode
            
    return -1

if __name__ == '__main__':
    N = int(input())
    link = [[] * N for _ in range(N)]
    # cycle_station[i] = 0 : 방문하지 않은 노드
    # cycle_station[i] = 1 : 방문한 노드
    # cycle_station[i] = 2 : 사이클에 속하는 노드
    cycle_station = [0] * N
    distance = [0] * N

    for _ in range(N):
        a, b = map(int, input().split())
        link[a - 1].append(b - 1)
        link[b - 1].append(a - 1)

    dfs(1, 0)

    queue = deque()
    for i in range(N):
        if cycle_station[i] == 2:
            queue.append(i)
            distance[i] = 0
            
        else:
            distance[i] = -1
            
    while queue:
        now = queue.popleft()
        
        for y in link[now]:
            if distance[y] == -1:
                queue.append(y)
                distance[y] = distance[now] + 1
                
    print(*distance)
    
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