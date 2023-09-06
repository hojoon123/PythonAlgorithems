import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    
    while q:
        x = q.popleft()

        if x == 100:
            print(board[x])
            break
        
        for i in range(1, 7):
            nx = x + i
            
            if nx <= 100 and not visited[nx]:
                if nx in ladder_snake.keys():
                    nx = ladder_snake[nx]
                
                if not visited[nx]:
                    visited[nx] = True
                    board[nx] = board[x] + 1
                    q.append(nx)
    


if __name__ == '__main__':
    n, m = map(int,input().split())
    
    ladder_snake = dict()
    for i in range(n + m):
        x, y = map(int,input().split())
        ladder_snake[x] = y

    board = [0] * 101
    visited = [False] * 101
    bfs()

'''
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)
사다리의 정보를 의미하는 x, y (x < y)
x번 칸에 도착하면, y번 칸으로 이동
뱀의 정보를 의미하는 u, v (u > v)
u번 칸에 도착하면, v번 칸으로 이동
1번 칸에서 시작해서 100번 칸
G예제 입력 2 
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
예제 출력 2 
5
'''