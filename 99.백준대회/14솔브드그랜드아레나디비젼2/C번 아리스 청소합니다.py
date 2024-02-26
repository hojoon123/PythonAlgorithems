from collections import deque
import sys
input = sys.stdin.readline

def solve(h,w,start,type1,type2):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    visited = [[0] * w for i in range(h)]
    cnt = 1
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] += 1
    # 먼지가 있는 곳 방문 -> 먼지 청소 -> 먼지 청소한 곳 재방문 2회에 쫑
    
    while q:
        r, c, d, state = q.popleft()
        if state: # 규칙표 A
            d = (d + type1[r][c]) % 4
            nr = dr[d] + r
            nc = dc[d] + c
            if nr < 0 or nc < 0 or nr >= h or nc >= w or visited[nr][nc] == 2:
                break
            if visited[nr][nc] == 0:
                state = True
            else:
                state = False
            visited[nr][nc] += 1
            q.append((nr,nc,d,state))
            
        else: # B
            d = (d + type2[r][c]) % 4
            nr = dr[d] + r
            nc = dc[d] + c
            if nr < 0 or nc < 0 or nr >= h or nc >= w or visited[nr][nc] == 2:
                break
            if visited[nr][nc] == 0:
                state = True
            else:
                state = False
            visited[nr][nc] += 1
            q.append((nr,nc,d,state))
            
        cnt += 1
            
    return cnt
    
def main():
    # 시계 방향 북 동 남 서 0 -> 북 1 -> 동 2 -> 남 3-> 서
    h, w = map(int,input().split())
    r, c , d = map(int,input().split())
    type1 = []
    type2 = []
    for i in range(h):
        type1.append(list(map(int,input().rstrip())))
    for i in range(h):
        type2.append(list(map(int,input().rstrip())))
    
    print(solve(h,w,(r,c,d,True),type1,type2))
        
    
    
    
if __name__ == "__main__":
    main()
