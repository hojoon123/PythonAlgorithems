from sys import stdin
input = stdin.readline

def dfs(x, y, cnt, start_X, start_Y, color):
    global ans
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    if ans == True:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if cnt >= 4 and nx == start_X and ny == start_Y:
            ans = True
            return
        
        if world[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, start_X, start_Y, color)
            visited[nx][ny] = 0
            
def start(n, m):
    for i in range(n):
        for j in range(m):
            start_X, start_Y = i, j
            visited[i][j] = 1
            
            dfs(i, j, 1, start_X, start_Y, world[i][j])
            
            if ans == True:
                return "Yes"
            
    return "No"

N, M = map(int,input().split())
world = [list(str(input().rstrip())) for i in range(N)]
visited = [[0] * M for i in range(N)]
ans = False

print(start(N, M))
'''
4개 이상이어야 함 출발점 끝 점 동일 해야 함
첫째 줄에 게임판의 크기 N, M
게임판의 상태 
점의 색은 알파벳 대문자 한 글자

사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"
예제 입력 1 
3 4
AAAA
ABCA
AAAA
예제 출력 1 
Yes
'''