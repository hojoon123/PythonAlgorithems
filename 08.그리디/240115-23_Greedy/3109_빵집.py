import sys
input = sys.stdin.readline

def dfs(x, y, r, c, dx, visited, world):
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny] == 0 and world[nx][ny] == '.':
            visited[nx][ny] = 1
            if ny == c - 1:
                return True
            
            if dfs(nx,ny , r, c, dx, visited, world):
                return True
    return False
        

def main():
    r, c = map(int,input().split())
    world = [list(map(str,input().rstrip())) for i in range(r)]
    visited = [[0]*c for i in range(r)]
    dx = [-1,0,1]
    cnt = 0

    for i in range(r):
        if dfs(i, 0, r, c, dx, visited, world):
            cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()
