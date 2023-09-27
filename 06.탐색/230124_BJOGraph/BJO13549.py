from sys import stdin
from collections import deque
input = stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    cnt[n] = 0
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(cnt[x])
            return
        
        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx <= max and cnt[nx] == -1:
                if nx == x * 2:
                    cnt[nx] = cnt[x]
                    q.appendleft(nx)
                else:
                    cnt[nx] = cnt[x] + 1
                    q.append(nx)

if __name__ == '__main__':
    n, k = map(int,input().split())
    max = 10 ** 5
    cnt = [-1] * (max + 1)
    bfs(n)

'''
N 일 때 걷는다면 1초 후에 N - 1 또는 N + 1로 이동
0초 후에 2* N의 위치로 이동
N(0 ≤ N ≤ 100,000)
K(0 ≤ K ≤ 100,000)
수빈이가 있는 위치 N과 동생이 있는 위치 K
수빈이가 동생을 찾는 가장 빠른 시간을 출력
예제 입력 1 
5 17
5 10 9 18 17
5 4 8 16 17
예제 출력 1 
4
'''