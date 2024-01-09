import sys
from collections import deque
input = sys.stdin.readline

def turn(direct):
    global d
    if direct == 'L':
        d = (d + 3) % 4
    else:
        d = (d + 1) % 4

if __name__ == '__main__':
    dr = [0,1,0,-1] # 0 동 1 남 2 서 3 북
    dc = [1,0,-1,0]
    d = 0
    n = int(input())
    k = int(input())
    world = [[0] * n for i in range(n)] # 월드 생성
    
    for i in range(k): # 사과 배치
        r, c = map(int,input().split())
        world[r - 1][c - 1] = 1
        
    l = int(input())
    snake_patton = dict()
    for i in range(l): # 뱀 패턴
        a, b = map(str,input().split())
        snake_patton[int(a)] = b
        
    world[0][0] = 2 # 시작 준비
    r = 0; c = 0
    cnt = 0
    sq = deque()
    sq.append((0,0))
    
    while 1: # 게임 시작
        cnt += 1
        r = r + dr[d]
        c = c + dc[d]
        if r < 0 or r >= n or c < 0 or c >= n: # 벽에 부딪힐 때
            break
        if world[r][c] == 1:
            world[r][c] = 2
            sq.append((r,c))
            if cnt in snake_patton:
                turn(snake_patton[cnt])
                
        elif world [r][c] == 0:
            world[r][c] = 2
            sq.append((r,c))
            pr,pc = sq.popleft()
            world[pr][pc] = 0
            if cnt in snake_patton:
                turn(snake_patton[cnt])
        
        else:
            break
    print(cnt)
                
    
    
        
'''
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

뱀은 처음에 오른쪽을 향한다
L: 왼쪽 D: 오른쪽
예제 입력 1 
6
3

3 4
2 5
5 3

3

3 D
15 L
17 D
예제 출력 1 
9
예제 입력 2 
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
예제 출력 2 
21
예제 입력 3 
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
예제 출력 3 
13

'''