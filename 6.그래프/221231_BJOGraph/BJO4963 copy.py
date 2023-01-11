import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  world[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and world[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  world = []
  cnt = 0
  for _ in range(h):
    world.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if world[i][j] == 1:
        dfs(i, j)
        cnt += 1
  
  print(cnt)
            


'''
무한 루프
첫째 줄에는 지도의 너비 w와 높이 h
w와 h는 50보다 작거나 같은 양의 정수
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다
섬의 개수를 출력

입력의 마지막 줄에는 0 0
예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
'''