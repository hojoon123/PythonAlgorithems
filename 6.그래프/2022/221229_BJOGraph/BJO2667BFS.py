import sys
from collections import deque
input = sys.stdin.readline
# 테스트 케이스가 한 가지이기에 그래프를 변형해도 괜찮음
# 카피를 사용하지 않아도 되어서 따로 방문표시 없이 그래프를 조정해서 문제 해결

def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
                
    return cnt

N = int(input())
house = []
graph = [list(map(int,input().rstrip())) for i in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(graph, i, j)
            house.append(cnt)
            
house.sort()
print(len(house))
for i in house:
    print(i)

            


'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)
N줄에는 각각 N개의 자료(0혹은 1)

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''