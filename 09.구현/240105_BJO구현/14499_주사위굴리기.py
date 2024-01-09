from collections import deque
import sys
input = sys.stdin.readline


def turn(dice, dir): # 동 서 북 남
    # 위 뒤 오 왼 앞 바닥
    a, b, c, d, e, f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 1: 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif dir == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    elif dir == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e
        
def solve(graph, n, m, x, y, dx, dy, k_list, dice):
    for i in k_list:
        x = dx[i] + x
        y = dy[i] + y
        
        if x < 0 or x >= n or y < 0 or y >= m:
            x -= dx[i]
            y -= dy[i]
            continue
        
        turn(dice, i)
        
        if graph[x][y] == 0:
            graph[x][y] = dice[-1]
        else:
            dice[-1], graph[x][y] = graph[x][y], 0
            
        print(dice[0])

def main():
    n,m,x,y,k = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]
    k_list = list(map(int,input().split()))
    dice = [0,0,0,0,0,0]
    dx = [0,0,0,-1,1] # 동 서 북 남
    dy = [0,1,-1,0,0]
    solve(graph, n, m, x, y, dx, dy, k_list, dice)
    
        
if __name__ == "__main__":
    main()
    
'''

'''