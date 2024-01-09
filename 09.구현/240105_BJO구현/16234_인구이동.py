from collections import deque
import sys
input = sys.stdin.readline

# 연합원들 찾기
def bfs(graph, n, a, b, l, r):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque()
    result = []
    q.append((a, b))
    result.append((a, b))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1:
                continue
            
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                visited[nx][ny] = 1
                q.append((nx, ny))
                result.append((nx, ny))
    
    return result

def main():
    global visited
    n, l, r = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    
    while 1:
        visited = [[0] * n for i in range(n)]
        flag = 0
        # 연합 찾기
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    country = bfs(graph, n, i, j, l, r)
                    l_ctry = len(country)
                    
                    if l_ctry > 1:
                        flag = 1
                        avgPeople = sum([graph[x][y] for x, y in country]) // l_ctry
                        for x, y in country:
                            graph[x][y] = avgPeople
        
        if flag == 0:
            break
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()
    
'''

'''