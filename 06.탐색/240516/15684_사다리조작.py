import sys
from collections import deque
input = sys.stdin.readline


def check(): # 1자로 내려가는지 확인하는 함수 1자로 내려가면 True 아니면 False
    for i in range(n): # 처음 시작할 사다리 번호
        start = i   
        for j in range(h):
            if graph[j][start]==1:
                start += 1
            elif start>0 and graph[j][start-1] == 1:
                start -= 1    
        if i != start:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    
    for i in range(x, h): # 행
        if i == x: # 현재 위치부터 진행
            now = y
        else: # 처음부터 탐색
            now = 0
            
        for j in range(now, n - 1):
            if graph[i][j] == 0: # 0인 경우 가로줄 만들고, 연속된 가로선을 만들지 않기 위해 j + 2호출
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0
                
if __name__ == '__main__':
    n,m,h = map(int, input().split())
    graph = [[0] * n for _ in range(h)]
    
    for i in range(m):
        a,b = map(int, input().split())
        graph[a-1][b-1] = 1
    
    ans = 4
    dfs(0,0,0)
    print(ans if ans < 4 else -1)