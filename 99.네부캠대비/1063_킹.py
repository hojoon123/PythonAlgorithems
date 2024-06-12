import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, n, king_loc, doll_loc, order_list):
    dx = [0,0,1,-1,-1,-1,1,1] # 오 왼 아 위 
    dy = [1,-1,0,0,1,-1,1,-1]
    d ={"R":3,"L":2,"B":1,"T":0,"RT":7,"LT":6,"RB":5,"LB":4}
    graph[king_loc[0]][king_loc[1]] = 1
    graph[doll_loc[0]][doll_loc[1]] = 2
    q = deque()
    q.append(king_loc)
    
    while q:
        x, y =q.popleft()
        if not order_list:
            break
        order = order_list.popleft()
        nx = x + dx[d[order]]
        ny = y + dy[d[order]]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            q.append((x,y))
            continue
        if graph[nx][ny] == 2:
            dnx = nx + dx[d[order]]
            dny = ny + dy[d[order]]
            if dnx < 0 or dnx >= 8 or dny < 0 or dny >= 8:
                q.append((x,y))
                continue
            graph[dnx][dny] = 2
            graph[nx][ny] = 1
            graph[x][y] = 0
            q.append((nx,ny))
        else:
            graph[nx][ny] = 1
            graph[x][y] = 0
            q.append((nx,ny))
    
    for i in range(8):
        for j in range(8):
            if graph[i][j] == 1:
                king = [j,i]
            elif graph[i][j] == 2:
                doll = [j,i]
                
    return (king, doll)
            
def main():
    loc ={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    graph = [[0 for i in range(8)] for j in range(8)]
    king, doll, n = map(str,input().rstrip().split())
    x, y = king
    king_loc = (int(y)-1,int(loc[x]))
    x, y = doll
    doll_loc = (int(y)-1,int(loc[x]))
    order_list = deque()
    
    for i in range(int(n)):
        order = str(input().rstrip())
        order_list.append(order)
        
    king, doll = bfs(graph, n, king_loc, doll_loc, order_list)
    for key in loc:
        if loc[key] == king[0]:
            king[0] = key
            king[1] += 1
        if loc[key] == doll[0]:
            doll[0] = key
            doll[1] += 1
    print(*king, sep='')
    print(*doll, sep='')
    
            
if __name__ == "__main__":
    main()