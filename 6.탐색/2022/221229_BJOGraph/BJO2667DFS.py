import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 테스트 케이스가 한 가지이기에 그래프를 변형해도 괜찮음
# 카피를 사용하지 않아도 되어서 따로 방문표시 없이 그래프를 조정해서 문제 해결

N = int(input())
graph = [[] for i in range(N)]
cnt = 0
house = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph[i] = list(map(int,input().rstrip()))

def dfs(x,y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
    return

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i,j)
            house.append(cnt)
            cnt = 0
            
house.sort()
house_cnt = len(house)
print(house_cnt)
for i in range(house_cnt):
    print(house[i])
            


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