import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        
        if x == r2 and y == c2:
            return board[x][y]
        
        for i in range(6):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))
    return -1

if __name__ == '__main__':
    dxy = [(-2,-1),(-2,+1),(0,-2),(0,2),(2,-1),(2,1)]
    n = int(input())
    r1, c1, r2, c2 = map(int,input().split())
    board = [[-1] * n for i in range(n)]
    print(bfs(r1,c1))

'''
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이

예제 입력 1 
7
6 6 0 1
예제 출력 1 
4
'''