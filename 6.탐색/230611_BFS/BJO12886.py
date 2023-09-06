import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(a, b, c):
    q = deque()
    q.append((a,b))
    total = a + b + c
    visited[a][b]
    while q:
        x, y = q.popleft()
        z = total - (x + y)
        if x == y == z:
            print(1)
            return
        
        for i, j in combinations((x,y,z), 2):
            if i < j:
                j -= i
                i += i
            elif i > j:
                i -= j
                j += j
            else:
                continue
            
            k = total - (i + j)
            i = max(i,j,k)
            j = min(i,j,k)
            
            if not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
    print(0)

if __name__ == '__main__':
    n, m, k = map(int,input().split())
    total = n + m + k
    visited = [[False]*total for _ in range(total)]
    
    if total % 3 != 0:
        print(0)
    else:
        bfs(n,m,k)

'''
X Y 가 만나면 X = X * 2 Y = Y - X
탈출조건 1보다 아래로 내려가거나 500 보다 높아지거나
돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력
예제 입력 1 
10 15 35
예제 출력 1 
1
예제 입력 2 
1 1 2
예제 출력 2 
0
'''