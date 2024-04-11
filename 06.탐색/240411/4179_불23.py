import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((s[0],s[1],'J'))
    q.append((f[0],f[1],'F'))
    cnt = 0
    
    while q:
        x,y,z = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx,ny)
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                if z == "J":
                    return cnt
                else:
                    continue
            if graph[nx][ny] == '.':
                q.append((nx,ny,z))
                graph[nx][ny] = z
                
            elif graph[nx][ny] == 'J' and z == 'F':
                q.append((nx,ny,z))
                graph[nx][ny] = z

        cnt += 1
        for i in range(n):
            if 'J' in graph[i]:
                break
        else:
            return 'IMPOSSIBLE'
        
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int,input().split())
    graph = []
    for i in range(n):
        a = list(input().rstrip())
        graph.append(a)
        for j in range(len(a)):
            if a[j] == 'J':
                s = [i,j]
            elif a[j] == 'F':
                f = [i,j]

    print(bfs())